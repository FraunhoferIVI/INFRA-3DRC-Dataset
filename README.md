# INFRA-3DRC-Dataset
This is the offical repository of INFRA-3DRC-Dataset, a public dataset comparised of 3D automotive Radar and RGB camera data generated using Intelligent roadside Infrastructure OR smart Infrastructure setup. It contains the dataset (to be downloaded using given links below), software development kit (SDK) to read and perform basic functions on the dataset, and related documentation.


## Overview
- [Introduction](#introduction)
- [Smart Infrastructure sensors setup](#smart-infrastructure-sensors-setup)
- [License](#license)
- [Dataset Format](#dataset-format)
- [Dataset](#dataset)
- [Annotations Format](#annotations-format)
- [SDK User Guide](#sdk-user-guide)
- [Acknowledgement](#acknowledgement)
- [Citation](#citation)
- [Links](#links)
- [Contact](#contact)

---

## Introduction
INFRA-3DRC-Dataset is the public dataset generated using smart infrastructure setup. It consists of calibrated, time-synchronized, and annotated sensor frames of 3D autotmotive radar and RGB mono-camera. Each radar frame contains point-wise annotation and each camera image is annotated in form of 2D bounding box(es). For completeness, calibrated and time-synchronized 3D lidar sensor frames are also included in the dataset, but these frames are not annotated.  
<br />
At present, dataset consists of 27 scenes recorded from different geographical locations in different light conditions - day light, twilight and night. STATISTICS TO WRITE  

---

## Smart Infrastructure sensors setup
* The setup consists of 
  * RGB mono camera (ids CP-5260 rev 2 with 8 mm lens C-mount)
  * 3D Automotive radar (continental LRR ARS548) 
  * 3D-Lidar (Ouster OS1-64 channels),

* All the sensors are mounted on the extendable tripod for modular and flexible data collection.

| Sensor setup (in lab) | Sensor setup (at roadside) | Sensor coordinates |
|---|---|---|
|<img align= "center" src = "docs/images/sensor_setup_lab.png" width = 200px>|<img align= "center" src = "docs/images/sensor_setup_roadside.jpg" width = 200px>|<img align= "center" src = "docs/images/sensor_coordinates.png" width = 200px>|
|Copyright image|Copyright image|Copyright image|

---

## License

* The dataset and the associated code is realeased under the CC BY-NC 4.0. [See here](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)
* Under this license, it is allowed to download and use only for research, teaching, and academic purpose only.
* Use of this dataset and associated code is prohibited to use for any commercial application.
* If in case, it is needed for commercial demand, then kindly contact us (see bottom of this page). 

---

## Dataset Format
```---
  ├── scene_01
    ├── camera_01
      ├── camera_01__annotation - contains json files for each camera image
      ├── camera_01__data - contains png files of camera images
    ├── radar_01
      ├── radar_01__annotation - contains json files for each radar frame
      ├── radar_01__data - contains pcd files for each radar frame
    ├── lidar_01
      ├── lidar_01__data - contains pcd files for each lidar frame
    ├── calibration.json - contains extrinsic and intrinsic calibration matrix
    └── scene.json - contains meta-data of the scene

  ├── scene_02
    ├── camera_01
      ├── camera_01__annotation
      ├── camera_01__data
    ├── radar_01
      ├── radar_01__annotation
      ├── radar_01__data
    ├── lidar_01
      ├── lidar_01__data
    ├── calibration.json
    └── scene.json
.....

  ├── scene_N
    ├── camera_01
      ├── camera_01__annotation
      ├── camera_01__data
    ├── radar_01
      ├── radar_01__annotation
      ├── radar_01__data
    ├── lidar_01
      ├── lidar_01__data
    ├── calibration.json
    └── scene.json
```

---

## Dataset

| scene | description | location | outside conditions | frames | size (GB) | Download |
|---|---|---|---|---|---|---|
| scene_01 | one bicycle crossing the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 102 | 0.7 | [Link](link) |
| scene_02 | Two cars moving in the same direction crosses the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 102 | 0.7 | [Link](link) |
| scene_03 | One adult (person) crossing the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 183 | 1.2 | [Link](link) |
| scene_04 | One car and one motorcycle crosses the traffic light junction when traffic lights just turned to green from red. | pedestrain crossing junction with traffic light | daylight, clear sky | 80 | 0.5 | [Link](link) |
| scene_05 | One adult (person) walks towards traffic junction, and one car crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 137 | 0.9 | [Link](link) |
| scene_06 | Two cars crossing the traffic light junction from opposite directions. | pedestrain crossing junction with traffic light | daylight, clear sky | 158 | 1.04 | [Link](link) |
| scene_07 | One bicycle rides towards crossing junction and waits at red light. In parallel, one car drives from the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 107 | 0.72 | [Link](link) |
| scene_08 | Four cars are crossing the junction in opposite directions | pedestrain crossing junction with traffic light | daylight, clear sky | 139 | 0.95 | [Link](link) |
| scene_09 | One bicycle moving away from junction and two cars are waiting at junction in opposite lanes due to red signal. In sometime, both cars cross the junction at green light and another bicycle reaches the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 123 | 0.84 | [Link](link) |
| scene_10 | Three cars in the same lane behind each other waiting at junction due to red signal. In sometime, signal turns to green, and all the cars start moving and cross the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 171 | 1.13 | [Link](link) |
| scene_11 | One group (two adults walking together and very close to each other) crosses the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 93 | 0.64 | [Link](link) |
| scene_12 | One group crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 83 | 0.57 | [Link](link) |
| scene_13 | One group crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 108 | 0.73 | [Link](link) |
| scene_14 | Two cars moving behind each other in same lane | multi-lane bidirectional straight road | twilight, clear sky | 97 | 0.67 | [Link](link) |
| scene_15 | four cars moving in two lanes in the same direction| multi-lane bidirectional straight road | twilight, clear sky | 94 | 0.67 | [Link](link) |
| scene_16 | one car moving | multi-lane bidirectional straight road | twilight, clear sky | 83 | 0.55 | [Link](link) |
| scene_17 | one bus moving | multi-lane bidirectional straight road | twilight, clear sky  | 42 | 0.3 | [Link](link) |
| scene_18 | One bus and two cars moving in opposite lanes | multi-lane bidirectional straight road | twilight, clear sky | 137 | 0.0 | [Link](link) |
| scene_19 | one adult, one bicycle | open parking | daylight, clear sky | 300 | 0.0 | [Link](link) |
| scene_20 | one car, one person | open parking |  daylight, clear sky | 300 | 0.0 | [Link](link) |
| scene_21 | one car, one bicycle | open parking |  daylight, clear sky | 300 | 0.0 | [Link](link) |
| scene_22 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |
| scene_23 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |
| scene_24 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |
| scene_25 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |
| scene_26 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |
| scene_27 | to be decided | multi-lane bidirectional straight road | night, clear sky | 400 | 0.0 | [Link](link) |

#### To download complete dataset - [Link](link)
---

## Annotations Format

* Camera Annotations

---

## SDK User Guide

---

## Acknowledgement


---

## Citation

---

## Links

---

## Contact Us
