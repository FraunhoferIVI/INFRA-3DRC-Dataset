## Annotation details

### class categories

* For work, only category names from json files are sufficient.
* In the given dataset, at present, instances of category child and truck are not available.

| category_id | supercategory | category name |
|---|---|---|
| 1 | person | adult |
| 2 | person | child |
| 3 | person | group |
| 4 | person | bicycle |
| 5 | vehicle | motorcycle |
| 6 | vehicle | car |
| 7 | vehicle | bus |
| 8 | vehicle | truck |

### Details of camera annotations 

* Each object in camera image is labeled with 2D bounding box (in pixel coordinates), object category and unique track id.  

#### Each json file of camera annotation contains following information

* Frame or image level information
    * **image id**: unique id given to each frame (camera and radar) of one scene
    * **image file name**: refer to the corresponding image file (.png) for cross-reference
    * **image height**: 1216 pixels
    * **image width**: 1920 pixels
* object instance information
    * **category id**: refer above table 
    * **super category**: refer above table 
    * **name**: refer above table 
    * **det id**: unique id in each frame, used to associate annotations in camera and radar. Annotation with same det id in radar and camera are from same object in that particular synchronized sensor frames.
    * **track id**: unique id of the object in the complete scene
    * **bbox**: 2D Bounding of the object defined in COCO format - [x top left corner, y top left corner, height, width] pixels 

There is also some other information given in camera json files regarding license, dataset name, version, etc., but it is not required to work with dataset.

### Details of 3D radar annotations 
Each radar point in one radar frame is labeled with unique instance id, object category and unique track id. This is known as point-wise instance segmentation of radar point cloud.  
Further, all the radar points belong to same object are grouped together.  
The rest of the points from background (including unwanted users) are assigned as background points and are group together in the json file. 

#### Definiton of radar parameters associated with each radar points

| parameter | unit | dytpe | definition |
|---|---|---|---|
| index | no unit| uint16 | unique index given to each radar point in one frame. |
| range | meter | float32 | direct distance of the radar point with respect to origin of the radar sensor - given in polar coordinates |
| azimuth_angle | radians | float32 | horizontal angle of the radar point with respect to origin of the radar sensor - given in polar coordinates |
| elevation_angle | radians | float32 | vertical angle of the radar point with respect to origin of the radar sensor - given in polar coordinates |
| range_rate | m/sec | float32 | doppler speed of the radar point. It is negative when object is moving towards sensor, and positive when object is moving away from the sensor |
| rcs | dBsm | float32 | radar cross section of the radar point |
| x | meter | float32 | longitudinal distance of the radar point from sensor origin - given in cartesian coordinates |
| y | meter | float32 | lateral distance of the radar point from sensor origin - given in cartesian coordinates |
| z | meter | float32 | vertical distance of the radar point from sensor origin - given in cartesian coordinates |


#### Each json file of 3D radar annotation contains following information

* Frame level information
    * **image id**: unique id given to each frame (camera and radar) of one scene
    * **image file name**: refer to the corresponding sychronized image file (.png) for cross-reference
    * **image height**: 1216 pixels
    * **image width**: 1920 pixels
    * **pcd file name**: name of the corresponding radar pcd file associated with json file, for cross-reference
    * **fields**: Each radar point is associated with following parameters in same order - ['index', 'range', 'azimuth_angle', 'elevation_angle', 'range_rate', 'rcs', 'x', 'y', 'z']
    * **dytpes**: ['uint16', 'float32', 'float32', 'float32', 'float32', 'float32', 'float32', 'float32', 'float32'] - in the same order of fields
    * **width**: total radar points in the frame 
    * **height**: 1 
    * **points**: total radar points in the frame. Redundunt to width
* object instance information