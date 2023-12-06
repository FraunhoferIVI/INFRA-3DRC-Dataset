#! /usr/bin/env python3
"""
Script Name: Infra3DRC.py

Description: 
This script provides an interface to work with one scene from INFRA-3DRC dataset.

Authors: Shiva Agrawal, Savankumar Bhanderi.

Requirements:
- NumPy
- opencv
"""

from pathlib import Path
from typing import Union, List
import json
import numpy as np
from .utils import SceneInfo, Calibration
from .frame import Frame


class Infra3DRC:
    def __init__(self, dataset_root: Union[Path, str], scene_number: int = None) -> None:
        """convinient class for handling INFRA-3DRC-dataset.

        Args:
            dataset_root (Union[Path, str]): root path where dataset is stored.
            scene_number (int): scene number to read. defaults to None. If None, `dataset_root` must point to single scene directory instead of the whole dataset.
        """

        assert Path(dataset_root).is_dir(), f"Directory does not exists: {dataset_root}."

        if scene_number is None:
            if "scene" in dataset_root.split("_")[-1]:
                # path to single scene is provided.
                self.scene_path = Path(dataset_root)
            else:
                raise ValueError("When `scene_number` is set to None, `dataset_root` must point to single scene directory.")
        else:
            self.dataset_root = Path(dataset_root)

            assert scene_number <= 25, f"scene number must be in range 1-25, not {scene_number}"
            self.scene_number = scene_number
            self.scene_path = self.dataset_root.joinpath(
                f"INFRA-3DRC_scene-{str(scene_number).zfill(2)}"
            )

        assert self.scene_path.is_dir(), f"Directory not found : {self.scene_path}"
        # read scene json
        self.scene_info = self._parse_scene_json()
        # read calibration json and set atributes accordingly
        self.calibration = self._parse_calibration_json()

        # list of pathlib.Path objects
        self.images_paths_list = sorted(
            self.scene_path.joinpath("camera_01", "camera_01__data").iterdir()
        )

        self.radar_pcds_paths_list = sorted(
            self.scene_path.joinpath("radar_01", "radar_01__data").iterdir()
        )

        self.camera_annot_paths_list = sorted(
            self.scene_path.joinpath("camera_01", "camera_01__annotation").iterdir()
        )

        self.radar_annot_paths_list = sorted(
            self.scene_path.joinpath("radar_01", "radar_01__annotation").iterdir()
        )

        self.lidar_pcds_paths_list = sorted(
            self.scene_path.joinpath("lidar_01", "lidar_01__data").iterdir()
        )

    def _parse_scene_json(self) -> SceneInfo:
        """reads scene.json file and return information about this scene."""

        scene_json_path = self.scene_path.joinpath("scene.json")
        assert scene_json_path.is_file()

        with open(str(scene_json_path), "r") as f:
            scene_dict = json.load(f)

        scene_info = SceneInfo(
            location=scene_dict["location"],
            weather=scene_dict["weather"],
            daylight=scene_dict["day_light"],
            description=scene_dict["description"],
            total_frames=scene_dict["total_frames_count"],
        )

        return scene_info

    def _parse_calibration_json(self):
        """reads the calibration json and returns the Calibration object which contains information about calibrations."""

        calibration_json_path = self.scene_path.joinpath("calibration.json")
        assert calibration_json_path.is_file()

        with open(str(calibration_json_path), "r") as f:
            calibration_dict = json.load(f)

        calibrations_list = calibration_dict["calibration"]

        for calibration_type in calibrations_list:
            if calibration_type["calibration"] == "lidar_01_to_camera_01":
                lidar_to_camera = np.array(calibration_type["T"])
            if calibration_type["calibration"] == "radar_01_to_camera_01":
                radar_to_camera = np.array(calibration_type["T"])
            if calibration_type["calibration"] == "lidar_01_to_ground":
                lidar_to_ground = np.array(calibration_type["T"])
            if calibration_type["calibration"] == "radar_01_to_lidar_01":
                radar_to_lidar = np.array(calibration_type["T"])
            if calibration_type["calibration"] == "camera_01":
                camera_intrinsics = np.array(calibration_type["k"])
                camera_distcoeffs = np.array(calibration_type["D"])

        calibration = Calibration(
            lidar_to_camera=lidar_to_camera,
            radar_to_camera=radar_to_camera,
            lidar_to_ground=lidar_to_ground,
            radar_to_lidar=radar_to_lidar,
            camera_intrinsics=camera_intrinsics,
            camera_distcoeffs=camera_distcoeffs,
        )
        return calibration

    def __iter__(self):
        for img_path, r_pcd_path, c_json_path, r_json_path, l_pcd_path in zip(
            self.images_paths_list,
            self.radar_pcds_paths_list,
            self.camera_annot_paths_list,
            self.radar_annot_paths_list,
            self.lidar_pcds_paths_list,
        ):
            yield Frame(
                img_path,
                r_pcd_path,
                c_json_path,
                r_json_path,
                l_pcd_path,
                self.calibration,
            )

    def __getitem__(self, indices):
        if isinstance(indices, int):
            image_path = self.images_paths_list[indices]
            radar_pcd_path = self.radar_pcds_paths_list[indices]
            camera_json_path = self.camera_annot_paths_list[indices]
            radar_json_path = self.radar_annot_paths_list[indices]
            lidar_pcd_path = self.lidar_pcds_paths_list[indices]

            return Frame(
                image_path=image_path,
                radar_pcd_path=radar_pcd_path,
                image_json_path=camera_json_path,
                radar_json_path=radar_json_path,
                lidar_pcd_path=lidar_pcd_path,
                calibration=self.calibration,
            )
            # return single frame, or slice of it
        if isinstance(indices, tuple):
            # multi index is stored as tuple. return list of frames.
            list_of_frames: List[Frame] = []
            for idx in indices:
                image_path = self.images_paths_list[idx]
                radar_pcd_path = self.radar_pcds_paths_list[idx]
                camera_json_path = self.camera_annot_paths_list[idx]
                radar_json_path = self.radar_annot_paths_list[idx]
                lidar_pcd_path = self.lidar_pcds_paths_list[idx]

                i_frame = Frame(
                    image_path=image_path,
                    radar_pcd_path=radar_pcd_path,
                    image_json_path=camera_json_path,
                    radar_json_path=radar_json_path,
                    lidar_pcd_path=lidar_pcd_path,
                    calibration=self.calibration,
                )
                list_of_frames.append(i_frame)
            return list_of_frames

    def __len__(self):
        return self.scene_info.total_frames

    def __str__(self):
        s = self.__class__.__name__ + "("
        s += f"scene_number={str(self.scene_number).zfill(2)}, "
        s += f"total_frames={len(self)})"
        return s

    __repr__ = __str__
