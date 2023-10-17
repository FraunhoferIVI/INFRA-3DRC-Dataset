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

---

## Introduction
INFRA-3DRC-Dataset is the public dataset generated using smart infrastructure setup. It consists of calibrated, time-synchronized, and annotated sensor frames of 3D autotmotive radar and RGB mono-camera. Each radar frame contains point-wise annotation and each camera image is annotated in form of 2D bounding box(es). For completeness, calibrated and time-synchronized 3D lidar sensor frames are also included in the dataset, but these frames are not annotated.  
<br />
At present, dataset consists of 27 scenes recorded from different geographical locations in different light conditions - day light, twilight and night. STATISTICS TO WRITE

<div align="center">
<p float="center">
<img src="" alt="" width="400"/>
<img src="" alt="" width="400"/>
<br />
<img src="" alt="" width="400"/>
<img src="" alt="" width="400"/>
<br />

</p>
</div>

---

## Smart Infrastructure sensors setup


---

## License

---

## Dataset Format
```---
  ├── scene_01
    ├── camera_01
      ├── camera_01__annotation: contains json files for each camera image
      ├── camera_01__data: contains png files of camera images
    ├── radar_01
      ├── radar_01__annotation: contains json files for each radar frame
      ├── radar_01__data: contains pcd files for each radar frame
    ├── lidar_01
      ├── lidar_01__data: contains pcd files for each lidar frame
    ├── calibration.json: contains extrinsic and intrinsic calibration matrix
    └── scene.json: contains meta-data of the scene
```
```---
  ├── scene_02
    ├── camera_01
      ├── camera_01__annotation: contains json files for each camera image
      ├── camera_01__data: contains png files of camera images
    ├── radar_01
      ├── radar_01__annotation: contains json files for each radar frame
      ├── radar_01__data: contains pcd files for each radar frame
    ├── lidar_01
      ├── lidar_01__data: contains pcd files for each lidar frame
    ├── calibration.json: contains extrinsic and intrinsic calibration matrix
    └── scene.json: contains meta-data of the scene
```
```---
  ├── scene_03
    ├── camera_01
      ├── camera_01__annotation: contains json files for each camera image
      ├── camera_01__data: contains png files of camera images
    ├── radar_01
      ├── radar_01__annotation: contains json files for each radar frame
      ├── radar_01__data: contains pcd files for each radar frame
    ├── lidar_01
      ├── lidar_01__data: contains pcd files for each lidar frame
    ├── calibration.json: contains extrinsic and intrinsic calibration matrix
    └── scene.json: contains meta-data of the scene
```

---

## Dataset

---

## Annotations Format

---

## SDK User Guide

---

## Acknowledgement

---

## Citation

---

## Links
