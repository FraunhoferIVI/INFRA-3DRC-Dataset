# INFRA-3DRC Dataset
This is the offical repository of INFRA-3DRC Dataset, a public dataset comparised of 3D automotive Radar and RGB camera data generated using Intelligent roadside Infrastructure (also known as smart Infrastructure) setup. It contains the links to download dataset, software development kit (SDK) to read and perform basic functions on the dataset, and related documentation.
<br/>
<br/>
This work is supported by the Bavarian Ministry of Economic Affairs, Regional Development and Energy (StMWi), Germany within the Project “InFra — Intelligent Infrastructure.”   



## Overview
- [Introduction](#introduction)
- [Smart Infrastructure sensors setup](#smart-infrastructure-sensors-setup)
- [License](#license)
- [Dataset Format](#dataset-format)
- [Dataset](#dataset)
- [Annotation Format](#annotation-format)
- [SDK User Guide](#sdk-user-guide)
- [Citation](#citation)
- [References](#references)
- [Contact](#contact)

---

## Introduction
INFRA-3DRC Dataset is the public dataset generated using smart infrastructure setup. It consists of calibrated, time-synchronized, and annotated sensor frames of 3D autotmotive radar and RGB mono-camera. Each radar frame contains point-wise annotation and each camera image is annotated in form of 2D bounding box(es). For completeness, calibrated and time-synchronized 3D lidar sensor frames are also included in the dataset, but these frames are not annotated.  
<br />
At present, dataset consists of 25 scenes recorded from different geographical locations in different light conditions - day light, twilight and night. STATISTICS TO WRITE  and 6 gifs to add in grid 

<img src="docs/gifs/01.gif" width="30%"></img> 
<img src="docs/gifs/01.gif" width="30%"></img> 
<img src="docs/gifs/01.gif" width="30%"></img> 
<img src="docs/gifs/01.gif" width="30%"></img> 
<img src="docs/gifs/01.gif" width="30%"></img> 
<img src="docs/gifs/01.gif" width="30%"></img> 

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
* If in case, it is needed for commercial use, then kindly contact us (see bottom of this page). 

---

## Dataset Format
```---
  ├── INFRA-3DRC_scene-01
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

  ├── INFRA-3DRC_scene-02
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

  ├── INFRA-3DRC_scene-NN
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

To download the dataset, refer the following page [DATASET-DOWNLOAD](docs/DOWNLOAD_DATASET.md)

---

## Annotation Format

Dataset contains annotations of 3D automotive radar sensor and RGB camera images. For details refer the following page [ANNOTATION-DETAILS](docs/ANNOTATION_DETAILS.md)

---

## SDK User Guide

Software development Kit (SDK) to use this dataset is available in the [GITHUB-REPO](https://github.com/FraunhoferIVI/INFRA-3DRC-Dataset). Further, for details about how to use this SDK, various functions, and demo examples, refer the following page [SDK-USER-GUIDE](docs/SDK_USER_GUIDE.md)

---

## Citation

to be added later

---

## References

to be added later

---

## Contact Us

to be added later
