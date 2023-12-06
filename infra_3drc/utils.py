#! /usr/bin/env python3
from dataclasses import dataclass
import numpy as np


@dataclass
class Detection:
    image_id: int
    det_id: int
    category_id: int
    track_id: int
    instance_id: int
    bbox: np.array
    points: np.recarray


@dataclass
class Calibration:
    lidar_to_camera: np.array
    radar_to_camera: np.array
    lidar_to_ground: np.array
    radar_to_lidar: np.array
    camera_intrinsics: np.array
    camera_distcoeffs: np.array


@dataclass
class SceneInfo:
    location: str
    weather: str
    daylight: str
    description: str
    total_frames: str
