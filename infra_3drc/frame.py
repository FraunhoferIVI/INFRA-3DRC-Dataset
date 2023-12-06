#! /usr/bin/env python3
"""
Script Name: frame.py

Description: 
This script provides functionality to process one synchronized frame of camera, radar, and lidar sensor.

Authors: Shiva Agrawal, Savankumar Bhanderi.

Requirements:
- NumPy
- opencv
"""

from pathlib import Path
from typing import Union, List
import json
import numpy as np
import cv2, ast, math
import re, random
from collections import OrderedDict
import struct
import numpy.lib.recfunctions as rfn
from .utils import Calibration, Detection
from .class_names import INFRA_ID_TO_CLASS

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

# this is a workaround for the qt "xcb" plugin error.
matplotlib.use("TkAgg")


class Frame:
    def __init__(
        self,
        image_path: Union[Path, str],
        radar_pcd_path: Union[Path, str],
        image_json_path: Union[Path, str],
        radar_json_path: Union[Path, str],
        lidar_pcd_path: Union[Path, str],
        calibration: Calibration,
    ) -> None:
        """represents one single frame of synchronized camera, radar and lidar data.

        Args:
            image_path (Union[Path, str]): path to camera image
            radar_pcd_path (Union[Path, str]): path to radar pcd
            image_json_path (Union[Path, str]): path to image annotation json
            radar_json_path (Union[Path, str]): path to radar annotation json
            lidar_pcd_path (Union[Path, str]): path to lidar pcd
            calibration (Calibration): Calibration object.
        """
        # synchronized frame paths
        self.image_path = image_path
        self.radar_pcd_path = radar_pcd_path
        self.image_json_path = image_json_path
        self.radar_json_path = radar_json_path
        self.lidar_pcd_path = lidar_pcd_path

        # calibration info
        self.calibration = calibration

        # properties
        self._radar_point_cloud = None
        self._lidar_point_cloud = None
        self._camera_image = None
        self._radar_background_cloud  = None

        # hardcoded type strings for PCD binary data decoding
        self.radar_typ_str = "<ffffffff"  # specific for point cloud from ARS548 radar
        self.lidar_typ_str = (
            "<fff4xfIHB1xH2xI4x4x4x"  # specific for point cloud from Ouster lidar
        )

        # annotation dicts
        self.camera_annot_dict = self._parse_annotation_json(self.image_json_path)
        self.radar_annot_dict = self._parse_annotation_json(self.radar_json_path)

        # sanity check.
        assert (
            self.camera_annot_dict["image"]["id"]
            == self.radar_annot_dict["image"]["id"]
        )
        self.image_id = self.camera_annot_dict["image"]["id"]

        # list of detections. each detection contain bbox, points, image_id, det_id, category_id, track_id, instance_id.
        self.objects: List[Detection] = self._get_objects()



    @property
    def camera_image(self):
        if self._camera_image is not None:
            return self._camera_image
        self._camera_image = cv2.imread(str(self.image_path))
        return self._camera_image

    @property
    def radar_point_cloud(self):
        if self._radar_point_cloud is not None:
            return self._radar_point_cloud
        self._radar_point_cloud = self._read_radar_pcd()
        return self._radar_point_cloud

    @property
    def radar_background_cloud(self):
        if self._radar_background_cloud is not None:
            return self._radar_background_cloud
                
        self._radar_background_cloud = self._points_list_to_recarray(
            self.radar_annot_dict["background"]
        )
        # radar annotation json contains background points up to 300 meters. clip it to 120.
        self._radar_background_cloud = self._radar_background_cloud[self._radar_background_cloud["x"] <= 120]
        # add u,v fields in background cloud.
        self._radar_background_cloud  = self.project_cloud_to_camera("radar", self._radar_background_cloud)
        # also the points not falling in image fov are not considered in background class. add them saperately here.
        raw_cloud = self.project_cloud_to_camera("radar", self.radar_point_cloud)
        clipped_cloud = self._clip_point_cloud_to_camera_fov(raw_cloud)
        points_outside_image = raw_cloud[np.isin(raw_cloud["index"], clipped_cloud["index"], invert=True)]

        if points_outside_image.shape[0] > 0:
            self._radar_background_cloud = np.append(self._radar_background_cloud, points_outside_image)
        
        # removing duplicated if any.
        self._radar_background_cloud = np.unique(self._radar_background_cloud)

        return self._radar_background_cloud


    @property
    def lidar_point_cloud(self):
        if self._lidar_point_cloud is not None:
            return self._lidar_point_cloud
        self._lidar_point_cloud = self._read_lidar_pcd()
        return self._lidar_point_cloud

    def _parse_annotation_json(self, json_path: Union[Path, str]) -> dict:
        """reads the json file and returns the dict.

        Args:
            json_path (Union[Path, str]): json path

        Returns:
            dict: annotation dict
        """
        json_path = Path(json_path)
        assert json_path.is_file(), f"file not found: {json_path.name}"
        with open(str(json_path), "r") as f:
            annot_dict = json.load(f)

        return annot_dict

    def _get_objects(self) -> List[Detection]:
        """read camera and radar objects and merge them into one object."""

        camera_objects = self.camera_annot_dict["annotations"]
        radar_objects = self.radar_annot_dict["objects"]

        # In all cases, the number of camera objects must be >= number of radar objecte
        assert len(camera_objects) >= len(radar_objects)

        objects = []
        for c_obj in camera_objects:
            det_id = c_obj["det_id"]
            track_id = None
            if c_obj.__contains__("track_id"):
                track_id = c_obj["track_id"]
            # sanity check , image id of each object and the entire json must be same.
            assert c_obj["image_id"] == self.image_id
            bbox = c_obj["bbox"]
            category_id = c_obj["category_id"]
            try:
                r_object = [
                    r_obj for r_obj in radar_objects if r_obj["det_id"] == det_id
                ][0]
                instance_id = r_object["instance_id"]
                points = r_object["points"]
                obj_points = self._points_list_to_recarray(points)
            except IndexError:
                instance_id = None
                obj_points = None

            det = Detection(
                image_id=self.image_id,
                det_id=det_id,
                category_id=category_id,
                track_id=track_id,
                instance_id=instance_id,
                bbox=bbox,
                points=obj_points,
            )
            objects.append(det)

        return objects

    def _points_list_to_recarray(self, point_list: list) -> np.recarray:
        """convert list of points list to numpy recarray

        Args:
            point_list (list): list of points

        Returns:
            np.recarray
        """

        fields = self.radar_annot_dict["radar_pcd_metadata"]["fields"]
        dtypes = self.radar_annot_dict["radar_pcd_metadata"]["dtypes"]

        np_dtype = np.dtype(
            {
                "names": ast.literal_eval(fields),
                "formats": ast.literal_eval(dtypes),
            }
        )

        points_cloud = np.rec.array(list(map(tuple, point_list)), np_dtype)
        return points_cloud

    def _pcd_metadata_template(self) -> OrderedDict:
        """pcd header template for reading the pcd"""

        metadata = OrderedDict(
            (
                ("VERSION", 0.7),
                ("FIELDS", []),
                ("SIZE", []),
                ("TYPE", []),
                ("COUNT", []),
                ("WIDTH", 0),
                ("HEIGHT", 0),
                ("VIEWPOINT", [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]),
                ("POINTS", 0),
                ("DATA", "binary"),
            )
        )

        return metadata

    def _read_pcd(self, pcd_path: Union[Path, str], sensor: str) -> np.recarray:
        """reads the pcd file for sensor.

        Args:
            pcd_path (Union[Path, str]): path ot pcd file.
            sensor (str): radar or lidar.

        Returns:
            np.recarray: pcd point cloud
        """

        assert pcd_path.is_file(), f"No pcd found at {str(pcd_path)}."
        # ordered dict for reading metadata information from pcd file.
        metadata = self._pcd_metadata_template()

        with open(str(pcd_path), "rb") as pcd_file:
            for line in pcd_file:
                ln = line.strip().decode("utf-8")
                # first line, or any line with  unimortant content.
                if ln.startswith("#") or len(ln) < 2:
                    continue
                # Regular expression matching with the data of the pcd header.
                match = re.match("(\w+)\s+([\w\s\.]+)", ln)
                # no match detected, meaning the header is faulty
                if not match:
                    print(f"warning: can't understand line: {ln}")
                    continue
                # header key, and values - all are strings
                key, value = match.group(1), match.group(2)

                if key == "VERSION":
                    pass

                # viewpoint format -  translation (tx ty tz) + quaternion (qw qx qy qz)
                if key == "VIEWPOINT":
                    metadata[key] = list(map(float, value.split()))
                # these fields should be converted into int data type - only one entry
                if key in ["POINTS", "HEIGHT", "WIDTH"]:
                    metadata[key] = int(value)
                # these fields belong to int, but list of entries
                if key in ["SIZE", "COUNT"]:
                    metadata[key] = list(map(int, value.split()))
                # convert single string to list of strings
                if key in ["TYPE", "FIELDS", "DATA"]:
                    metadata[key] = value.split() if len(value.split()) > 1 else value

                # here begins the actual binary data
                if ln.startswith("DATA"):
                    break

            # starting byte index.
            start = 0
            # list of points.
            cloud = []
            # actual binary data
            binary_data = pcd_file.read()

            # list of byte sizes for each of the pointfields. - used for decoding the binary data.
            field_sizes = [
                metadata["SIZE"][i] * metadata["COUNT"][i]
                for i in range(len(metadata["SIZE"]))
            ]

            if sensor.lower() == "radar":
                # type string to get the dtype information for binary decoding of radar pcd.
                type_str = self.radar_typ_str
                # list of numpy data types for each fields for converting list of points to numpy record array.
                np_dtypes = [
                    (field, np.dtype(typ_str))
                    for field, typ_str in zip(metadata["FIELDS"], type_str[1:])
                ]
            if sensor.lower() == "lidar":
                # type string to get the dtype information for binary decoding of lidar pcd.
                type_str = self.lidar_typ_str
                # lidar pcds contain extra pading bytes from the sensor. generating numpy dtypes considering that fact.
                np_dtypes = [
                    (field, np.dtype(typ))
                    for field, typ in zip(
                        metadata["FIELDS"], type_str[1:].replace("x", "")
                    )
                    if not field == "PAD"
                ]

            # binary decoding in the chunks of sum(field_sizes).
            for pts in range(metadata["POINTS"]):
                # index slice for decoding current point.
                end = start + sum(field_sizes)
                pt = struct.unpack(type_str, binary_data[start:end])
                cloud.append(pt)
                start = end
            # list of lists to numpy record array.
            cloud_np = np.rec.array(cloud, dtype=np_dtypes)

            # adding extra "index" field to keep track of point index.
            if "index" not in cloud_np.dtype.names:
                d_type = np.dtype({"names": ["index"], "formats": [np.uint32]})
                seq = np.linspace(
                    0,
                    cloud_np.shape[0],
                    cloud_np.shape[0],
                    endpoint=False,
                    dtype=d_type,
                )
                cloud_np = rfn.merge_arrays(
                    (seq, cloud_np), flatten=True, asrecarray=True
                )

        # we only have radar points annotations till 120 meters. 
        # so, we clip the raw radar cloud to 120 meters in x.
        if sensor == "radar":
            cloud_np = cloud_np[cloud_np["x"] <= 120]

        return cloud_np

    def draw_annotations(self, display=False) -> np.array:
        """draws image annotaions on camera image.

        Args:
            display (bool, optional): Whether to display the annotated image. If True, displays the image along side of returning it.
                        Defaults to False.

        Returns:
            np.array: camera image with annotaions drawn. (2D bbox, class, 3D radar points, and track id info.)
        """
        assert self.objects

        # random colors for drawing the bounding boxes and the 3D radar points.
        blue = random.sample(range(100, 255), 100)
        green = random.sample(range(70, 200), 100)
        red = random.sample(range(50, 255), 100)
        # expecting less than 100 object in the frame.
        colors = [(blue[i], green[i], red[i]) for i in range(100)]

        cv_image = self.camera_image.copy()

        for obj in self.objects:
            cat_id = obj.category_id
            track_id = obj.track_id
            x0, y0, w, h = obj.bbox
            x1, y1 = int(x0 + w), int(y0 + h)
            points = (
                obj.points
            )  # it will be none for those objects which does not have any radar points.
            color = colors[track_id]
            class_name = INFRA_ID_TO_CLASS[str(cat_id)]["name"]
            cv2.rectangle(cv_image, (int(x0), int(y0)), (x1, y1), color, 3)
            fontScale = 0.8 
            if points is not None:
                points = self.project_cloud_to_camera(mode="radar", cloud=points)
                for obj_pt in points:
                    u, v = int(obj_pt["u"]), int(obj_pt["v"])
                    cv_image = cv2.circle(cv_image, (int(u), int(v)), 7, color, -1)

                # update the fontscale for bounding box text label based on the distance of the object.+
                if points["range"].mean() > 50:
                    fontScale = 1.0

            text_label = f"{str(track_id).zfill(2)}: {class_name}"

            thickness = 1 
            (w1, h1), _ = cv2.getTextSize(
                text_label, cv2.FONT_HERSHEY_TRIPLEX, fontScale, thickness
            )

            cv2.rectangle(
                cv_image,
                (int(x0), int(y0 - (h1 + 0.6 * h1))),
                (int(x0 + (w1 + 0.1 * w1)), int(y0 - 0.1 * h1)),
                (0, 0, 0),
                -1,
                cv2.LINE_AA,
            )

            cv_image = cv2.putText(
                cv_image,
                text_label,
                (int(x0), int(y0 - (0.5 * h1))),
                cv2.FONT_HERSHEY_TRIPLEX,
                fontScale,  # fontscale
                (255, 255, 255),
                thickness,  # thickness
                cv2.LINE_AA,
            )
        cv_image = cv2.addWeighted(cv_image, 0.8, self.camera_image.copy(), 0.2, 0)
        if display:

            cv2.namedWindow("Ground Truth Annotations", cv2.WINDOW_KEEPRATIO)
            cv2.imshow("Ground Truth Annotations", cv_image)
            while cv2.getWindowProperty('Ground Truth Annotations', cv2.WND_PROP_VISIBLE) >= 1 : #cv2.WND_PROP_VISIBLE
                keyCode = cv2.waitKey(500)
            
                if (keyCode & 0xFF) == ord("q"):
                    cv2.destroyAllWindows()
                    break
                    
        return cv_image

    def _read_radar_pcd(self) -> np.recarray:
        radar_cloud = self._read_pcd(self.radar_pcd_path, "radar")
        return radar_cloud

    def _read_lidar_pcd(self) -> np.recarray:
        lidar_cloud = self._read_pcd(self.lidar_pcd_path, "lidar")
        return lidar_cloud

    def _3D_vis(self, mode: str, camera_fov_align: bool) -> None:
        mode = mode.lower()
        assert mode in ["radar", "lidar"]

        if mode == "radar":
            cloud = self.radar_point_cloud
            size = 1
        if mode == "lidar":
            cloud = self.lidar_point_cloud

        if camera_fov_align:
            cloud = self.project_cloud_to_camera(mode=mode, cloud=cloud)
            cloud = self._clip_point_cloud_to_camera_fov(cloud)

        locs = cloud[["x", "y", "z"]]
        if mode == "lidar":
            locs["z"] = locs["z"] - 3.5

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection="3d")
        scatter = ax.scatter3D(locs["x"], locs["y"], locs["z"], color="red", marker=".")
        ax.set_xlabel("X (metres)")
        ax.set_ylabel("Y (metres)")
        ax.set_zlabel("Z (metres)")

        # ax.set_facecolor("black")
        ax.grid(True, color="white", linestyle="dotted")

        fig.canvas.mpl_connect(
            "pick_event",
            lambda event: print(
                f"Point3D(X={locs['x'][event.ind[0]]},Y={locs['x'][event.ind[0]]},Z={locs['x'][event.ind[0]]})"
            ),
        )
        scatter.set_picker(True)
        plt.show()

    def visualise_3D_radar_point_cloud(self, camera_fov_align=False) -> None:
        """spawns a matlab 3D interactive scatter plot for visualizing 3D radar point cloud.

        Args:
            camera_fov_align (bool, optional): _description_. Defaults to False.
        """

        self._3D_vis(mode="radar", camera_fov_align=camera_fov_align)

    def visualise_3D_lidar_point_cloud(self, camera_fov_align=False):
        raise NotImplementedError

    def project_cloud_to_camera(self, mode: str, cloud: np.recarray) -> np.recarray:
        """calculate u,v positions of each point within cloud.
        Note that this function does not remove the points which do not fall on image plane. 

        Args:
            mode (str): radar and lidar
            cloud (np.recarray): sensor point cloud. Must contain [index,x,y,z] fields.

        Returns:
            np.recarray : projected cloud. Original point cloud with each points having two extra fields (columns) : u,v.
        """

        assert mode.lower() in ["radar", "lidar"]

        camera_instrinsics = self.calibration.camera_intrinsics
        if mode == "lidar":
            extrinsics = self.calibration.lidar_to_camera
        else:
            extrinsics = self.calibration.radar_to_camera

        # need (n,4) dimensions, 4th col values = 1
        cloud_xyz = cloud[["x", "y", "z", "index"]].copy()  # (n,4)
        cloud_xyz["index"] = 1  # (n,4)-[x,y,z,index(dummy)]
        # index array to keep track of points
        index = cloud["index"]
        # projection matrix
        p = np.matmul(camera_instrinsics, extrinsics)  # (3,3)*(3,4) -> (3,4)
        # multiply points in 3d sensor dim to projection matrix to get u,v,w
        projected_points = np.matmul(
            p, rfn.structured_to_unstructured(cloud_xyz).transpose()
        )  # (3,4)*(4,n) -> (3,n)
        w = projected_points[2, :]
        # camera has only 2d, but each point in projected_points is 3 dimensional(u,v,w)
        # normalise each point by third dim (w) to get the actual pixel coord of point
        projected_points = np.array(
            [
                projected_points[0, :] / projected_points[2, :],  # u = x/w
                projected_points[1, :] / projected_points[2, :],  # v = y/w
            ]
        )  # (2,n)
        projected_points = np.transpose(projected_points)  # (n,2) - (u,v)

        projected_points = np.column_stack((index, projected_points))

        dtype = np.dtype(
            {
                "names": ["index", "u", "v"],
                "formats": [np.uint32, np.float32, np.float32],
            }
        )

        projected_points = rfn.unstructured_to_structured(projected_points, dtype=dtype)

        if projected_points.size == 0:
            return None

        indices = [
            idx
            for idx, _ in enumerate(cloud["index"])
            if _ in projected_points["index"]
        ]
        raw_points_on_image = cloud[indices]

        points_with_uv = rfn.merge_arrays(
            (raw_points_on_image, projected_points[["u", "v"]]),
            flatten=True,
            asrecarray=True,
        )

        return points_with_uv

    def _clip_point_cloud_to_camera_fov(self, point_cloud: np.recarray) -> np.recarray:
        """clips the input point cloud to the cmaera field of view.

        Args:
            point_cloud (np.recarray): input point cloud. The cloud must have "u", and "v" fields.

        Returns:
            np.recarray : clipped cloud
        """
        cv_image = self.camera_image.copy()
        (rows, cols, channels) = cv_image.shape

        point_cloud = point_cloud[
            (point_cloud["u"] > 0)
            & (point_cloud["v"] > 0)
            & (point_cloud["u"] < cols)
            & (point_cloud["v"] < rows)
        ]
        return point_cloud

    def visualise_radar_cloud_on_camera(self, display=False) -> np.array:
        """project radar point cloud on camera image.

        Returns:
            np.array: projected image.
        """

        radar_cloud = self.radar_point_cloud
        projected_cloud = self.project_cloud_to_camera(mode="radar", cloud=radar_cloud)

        cv_image = self.camera_image.copy()
        projected_cloud = self._clip_point_cloud_to_camera_fov(projected_cloud)

        for point in projected_cloud:
            u, v = point["u"], point["v"]
            range_rate = point["range_rate"]
            if range_rate >= 0.1:
                cv_image = cv2.circle(cv_image, (int(u), int(v)), 5, (255, 0, 0), -1)
            elif range_rate <= -0.1:
                cv_image = cv2.circle(cv_image, (int(u), int(v)), 5, (0, 0, 255), -1)
            else:
                cv_image = cv2.circle(cv_image, (int(u), int(v)), 4, (0, 255, 0), -1)

        if display:
            cv2.namedWindow("Radar Projected on Image", cv2.WINDOW_KEEPRATIO)
            cv2.imshow("Radar Projected on Image", cv_image)

            while cv2.getWindowProperty('Radar Projected on Image', cv2.WND_PROP_VISIBLE) >= 1 : #cv2.WND_PROP_VISIBLE
                keyCode = cv2.waitKey(500)
            
                if (keyCode & 0xFF) == ord("q"):
                    cv2.destroyAllWindows()
                    break

        return cv_image

    def visualise_lidar_cloud_on_camera(self, display=False) -> np.array:
        """project lidar point cloud on camera image.

        Returns:
            np.array: projected image.
        """

        lidar_cloud = self.lidar_point_cloud
        projected_cloud = self.project_cloud_to_camera(mode="lidar", cloud=lidar_cloud)

        cv_image = self.camera_image.copy()
        projected_cloud = self._clip_point_cloud_to_camera_fov(projected_cloud)
        reflectivity = projected_cloud["reflectivity"]
        projected_cloud["reflectivity"] = (reflectivity - np.min(reflectivity)) / (
            np.max(reflectivity) - np.min(reflectivity)
        )

        for point in projected_cloud:
            u, v = point["u"], point["v"]

            cv_image = cv2.circle(
                cv_image,
                (int(u), int(v)),
                2,
                (int(point["reflectivity"] * 255), 70, 150),
                -1,
            )

        if display:
            cv2.namedWindow("Lidar projected on Image", cv2.WINDOW_KEEPRATIO)
            cv2.imshow("Lidar projected on Image", cv_image)
            while cv2.getWindowProperty('Lidar projected on Image', cv2.WND_PROP_VISIBLE) >= 1 : #cv2.WND_PROP_VISIBLE
                keyCode = cv2.waitKey(500)
            
                if (keyCode & 0xFF) == ord("q"):
                    cv2.destroyAllWindows()
                    break

        return cv_image

    def __iter__(self):
        for obj in self.objects:
            yield obj

    def __len__(self):
        return len(self.objects)

    def __getitem__(self, indices):
        return self.objects[indices]
        # if isinstance(indices, (int, slice)):
        #     return self.objects[indices]
        # return [Detection(self.objects[i], self.image) for i in indices]

    def __str__(self):
        s = self.__class__.__name__ + "("
        s += f"image_id={str(self.image_id)}, "
        s += f"num_objs={len(self.objects)}, "
        s += f"image_name={str(self.image_path.name)}, "
        s += f"radar_pcd_name={str(self.radar_pcd_path.name)}, "
        s += f"lidar_pcd_name={str(self.lidar_pcd_path.name)})"
        return s

    __repr__ = __str__
