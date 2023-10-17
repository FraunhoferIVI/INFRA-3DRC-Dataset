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
|<img align= "center" src = "docs/sensor_setup_lab_.png" width = 200px>|<img align= "center" src = "docs/sensor_setup_roadside_.jpg" width = 200px>|<img align= "center" src = "docs/sensor_coordinates.png" width = 200px>|
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

| scene | road users | outside conditions | frames | size (GB) | Download |
|---|---|---|---|---|---|
| scene_01 | one bicycle | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_02 | two cars | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_03 | one adult | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_04 | one car, one motorcycle | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_05 | one car, one adult | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_06 | two cars | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_07 | one bicycle, one car | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_08 | four cars | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_09 | two cars, two bicycles | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_10 | three cars | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_11 | one group | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_12 | one group | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_13 | one group | daylight, clear sky | 100 | 0.0 GB | [Link](link) |
| scene_14 | two cars | twilight, clear sky | 200 | 0.0 GB | [Link](link) |
| scene_15 | four cars | twilight, clear sky | 200 | 0.0 GB | [Link](link) |
| scene_16 | one car | twilight, clear sky | 200 | 0.0 GB | [Link](link) |
| scene_17 | one bus | twilight, clear sky | 200 | 0.0 GB | [Link](link) |
| scene_18 | one bus, two cars | twilight, clear sky | 200 | 0.0 GB | [Link](link) |
| scene_19 | one adult, one bicycle | daylight, clear sky | 300 | 0.0 GB | [Link](link) |
| scene_20 | one car, one person | daylight, clear sky | 300 | 0.0 GB | [Link](link) |
| scene_21 | one car, one bicycle | daylight, clear sky | 300 | 0.0 GB | [Link](link) |
| scene_22 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |
| scene_23 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |
| scene_24 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |
| scene_25 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |
| scene_26 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |
| scene_27 | to be decided | night, clear sky | 400 | 0.0 GB | [Link](link) |

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
