# USAGE

## Creating Infra3DRC object for the given scene.

```python
from Infra3DRC import Infra3DRC

# Please do not rename the folder after downloading the dataset. 
# Use this code snippet if you have downloaded entire dataset.
# path to the directory where dataset is saved.
dataset_root = "/path/to/infra_3drc_dataset"
# scene number to read.
scene_number = 1 
Infra3DRC_scene = Infra3DRC(dataset_root, scene_number)

# Use this code snippet if you have downloaded only one scene from the dataset. 
scene_path = "/path/to/single/scene"
# Scene number must be None when providing path to single scene folder.
scene_number = None 
Infra3DRC_scene = Infra3DRC(dataset_root, scene_number)
```
## Accesing calibration information from the scene.
The Infra3DRC class has an atribute **calibration** that allows user to access the calibration information for the scene.

```python
# this returns a calibration object which contains multi sensor calibrtaion matrices.
calibration = Infra3DRC_scene.calibration
# we can access individual calibration matrices using following syntax.
lidar_to_camera_extrinsics = calibration.lidar_to_camera
radar_to_camera_extrinsics = calibration.radar_to_camera
lidar_to_ground_extrinsics = calibration.lidar_to_ground
radar_to_lidar_extrinsics = calibration.radar_to_lidar
camera_intrinsics = calibration.camera_intrinsics
camera_distcoeffs = calibration.camera_distcoeffs
```
## Accesing scene environment information from the scene.
The Infra3DRC class has an atribute **scene_info** that allows user to access the scene information for the scene.

```python
# this returns a scene_info object which contains metadata about the scene.
scene_info = Infra3DRC_scene.scene_info
scene_description = scene_info.description
weather = scene_info.weather
location = scene_info.location
daylight = scene_info.daylight
total_frames_count = scene_info.total_frames
```
## Accesing synchronized frames from the scene.

The Infra3DRC class supports indexing. It returns a Frame object for the given index.
The frame object represents one temporally synchronized frame of camera, radar, and lidar sensor. 

```python
# index of the frame to read from current scene.
frame_number = 4
# this returns a Frame object for `frame_number` synchronized frame of camera, radar and lidar sensor.
frame = Infra3DRC_scene[frame_number]

# READING RAW CAMERA IMAGE FROM THE FRAME OBJECT.
camera_image = frame.camera_image

# READING POINT CLOUDS FROM THE FRAME OBJECT.
# each point cloud is of type np.recarray with field names assigned to each column.
# raw radar point cloud column names = ["index", "range", "azimuth_angle", "elevation_angle", "range_rate", "rcs", "x", "y", "z"].
radar_point_cloud = frame.radar_point_cloud
# this is the radar point cloud that is labeled as backgroud points.
radar_background_cloud = frame.radar_background_cloud

"""IMPORTANT NOTE ABOUT RADAR DATA.

Note that the 3D radar point cloud from the ARS 548 sensor contains data up to 300 meters in the x direction. 
However, we clip the radar point cloud to 120 meters beacause we only have ground truth annotations up to 120 meters.
The same is also applied to radar_background_cloud.
The background cloud from annotation json file may contain some duplicate points. These are removed when reading the json file.
If you are reading the json file independently, please use np.unique() function to remove any possible duplicates from numpy reacarray.
"""

# raw lidar point cloud column names = ["index", "x", "y", "z", "intensity", "t", "reflectivity", "ring", "ambient", "range"]
# NOTE : lidar pcd reading is computationally intensive due to large number of points., so it takes some time to run the following one line of code.
lidar_point_cloud = frame.lidar_point_cloud

# We can extract individual fields from each point clouds by running point_cloud["field_name"]
# for example, to extract velocity information from radar point cloud, we can use following code.
radar_velocity = radar_point_cloud["range_rate"]

# similiarly we can also iterate over the Infra3DRC object.
for frame_idx, frame in enumerate(Infra3DRC_scene):
    # actual logic to process one frame.
```
For more information on working with numpy recarrays, please visit the [official numpy documentation](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html).

## Visualising the point cloud on image plane.

To visualise radar or lidar point cloud on image plane, run the following code: 

```python
# if display is True, it will show projected the image on screen, and also return it, otherwise the function will only return the image with point cloud drawn on it.
display = True
# this returns a np.array (image) with radar point cloud drawn on it.
radar_overlayed_on_camera_image = frame.visualise_radar_cloud_on_camera(display=display)
# this returns a np.array (image) with lidar point cloud drawn on it.
lidar_overlayed_on_camera_image = frame.visualise_lidar_cloud_on_camera(display=display)

# Additionaly, the following functionality is provided for projecting the point cloud on the image. 
# this will calculate pixel positions of each point of point cloud, and add new columns for u,v in the original cloud.
projected_radar_point_cloud = frame.project_cloud_to_camera(mode="radar",cloud=frame.radar_point_cloud)
projected_lidar_point_cloud = frame.project_cloud_to_camera(mode="lidar",cloud=frame.lidar_point_cloud)
```
Subsequently, visualize the image using opencv or matplotlib visualizer.
TODO - embedd example image of radar and lidar point cloud drawn on camera image.

## Visualising the 3D Radar point cloud as an interactive plot.
The 3D radar point cloud of current frame can be visualised as a 3D interactive plot using the following functionality.
```python
# turn this flag to True if you want to plot only those radar points which fall within camera field of view.
camera_fov_align = False
# this will spawn a matlab 3D interactive scatter plot.
frame.visualise_3D_radar_point_cloud(camera_fov_align)
```
The visualization of 3D lidar point cloud is not implement due to large number of points. The user can use any third party libraries that handle 3D point clouds to visualize the lidar point cloud. Alternatively, the user can also use ros to visualize the raw pcds in rviz.

## Iterating over a Frame object.

The Frame object support indexing and iteration. The return type is Detection which corresponds to one labeled object (camera and radar only) in the frame.

```python
# this returns object of type Detection. The frame has total len(frame) number of labeled ground truth objects.
ith_gt_object = frame[i]

# the following sytanx can be used to extract object (detection) level information.
image_id = ith_gt_object.image_id
det_id = ith_gt_object.det_id
category_id = ith_gt_object.category_id
track_id = ith_gt_object.track_id
instance_id = ith_gt_object.instance_id
bbox = ith_gt_object.bbox # bbox in [ x0, y0, w, h]
points = ith_gt_object.points

# alternatively, we can also iterate over the labeled ground truth objects in the current frame.
for gt_obj in frame:
    # code to process one ground truth object.

# to get a list of all the ground truth objects
gt_objects = frame.objects
```

## Visualising the ground truth annotations in image plane.
The ground truth annotations for the Frame object can be visualised using the following syntax.
```python
# If display is true, the function visualises the annotates image along with returning it.
display = True
annotated_image = frame.draw_annotations(display=display)
```