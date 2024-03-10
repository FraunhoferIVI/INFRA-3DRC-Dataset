
## INFRA-3DRC Dataset

Dataset can be downloaded in parts (scene-wise) or in full. 

<span style="color:red"> ATTENTION - SOME TEMPORARY BUG FIXES </span>
* **For scene_18**, after downloading the dataset, only replace the downloaded **calibration.json** by this file - [calibration.json](/docs/fixes/calibration.json)
* **For scene_20**, after downloading the dataset, only replace the downloaded **scene.json** by this file - [scene.json](/docs/fixes/scene.json)

* **For all the scenes**, in each **calibration.json** file the correct extrinsic calibration matrix for ```lidar_01_to_ground```  is ```[ [1,0,0,0], [0,1,0,0], [0,0,1,3.5] ]```



| scene | description | location | outside conditions | frames | size (GB) | Download |
|---|---|---|---|---|---|---|
| scene_01 | one bicycle crossing the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 102 | 0.7 | [Link](https://fordatis.fraunhofer.de/retrieve/b5dcb0fd-b1b7-48f2-95be-4e4456b0a8fb/INFRA-3DRC_scene-01.zip) |
| scene_02 | Two cars moving in the same direction crosses the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 102 | 0.7 | [Link](https://fordatis.fraunhofer.de/retrieve/42a18066-4d32-4a04-b9de-563359526b71/INFRA-3DRC_scene-02.zip) |
| scene_03 | One adult (person) crossing the traffic light junction | pedestrain crossing junction with traffic light | daylight, clear sky | 183 | 1.2 | [Link](https://fordatis.fraunhofer.de/retrieve/493490ed-ef99-4cf3-aa0e-8ffb3647af16/INFRA-3DRC_scene-03.zip) |
| scene_04 | One car and one motorcycle crosses the traffic light junction when traffic lights just turned to green from red. | pedestrain crossing junction with traffic light | daylight, clear sky | 80 | 0.5 | [Link](https://fordatis.fraunhofer.de/retrieve/b37ae64e-86ef-4fd7-a87d-77089dd169b5/INFRA-3DRC_scene-04.zip) |
| scene_05 | One adult (person) walks towards traffic junction, and one car crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 137 | 0.9 | [Link](https://fordatis.fraunhofer.de/retrieve/49715d15-f037-4e63-94ab-969b269c7645/INFRA-3DRC_scene-05.zip) |
| scene_06 | Two cars crossing the traffic light junction from opposite directions. | pedestrain crossing junction with traffic light | daylight, clear sky | 158 | 1.04 | [Link](https://fordatis.fraunhofer.de/retrieve/37df8936-f3bf-476f-bc0a-b28b1402e9ff/INFRA-3DRC_scene-06.zip) |
| scene_07 | One bicycle rides towards crossing junction and waits at red light. In parallel, one car drives from the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 107 | 0.72 | [Link](https://fordatis.fraunhofer.de/retrieve/d4360900-0293-4bfa-b586-7db4d8d97be8/INFRA-3DRC_scene-07.zip) |
| scene_08 | Four cars are crossing the junction in opposite directions | pedestrain crossing junction with traffic light | daylight, clear sky | 139 | 0.95 | [Link](https://fordatis.fraunhofer.de/retrieve/5cc66ea8-6ebb-4e02-81a8-161f38e4fa37/INFRA-3DRC_scene-08.zip) |
| scene_09 | One bicycle moving away from junction and two cars are waiting at junction in opposite lanes due to red signal. In sometime, both cars cross the junction at green light and another bicycle reaches the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 123 | 0.84 | [Link](https://fordatis.fraunhofer.de/retrieve/cc320411-4dcc-4b5a-9149-5d9c46537f58/INFRA-3DRC_scene-09.zip) |
| scene_10 | Three cars in the same lane behind each other waiting at junction due to red signal. In sometime, signal turns to green, and all the cars start moving and cross the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 171 | 1.13 | [Link](https://fordatis.fraunhofer.de/retrieve/ab22878e-2b45-4f65-bc07-e504b295096f/INFRA-3DRC_scene-10.zip) |
| scene_11 | One group (two adults walking together and very close to each other) crosses the junction. | pedestrain crossing junction with traffic light | daylight, clear sky | 93 | 0.64 | [Link](https://fordatis.fraunhofer.de/retrieve/cfd36e01-c4b1-46ea-833e-2ab2b60abf34/INFRA-3DRC_scene-11.zip) |
| scene_12 | One group crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 83 | 0.57 | [Link](https://fordatis.fraunhofer.de/retrieve/a05edbfa-044b-4bdd-b96c-363cdff1faf6/INFRA-3DRC_scene-12.zip) |
| scene_13 | One group crosses the junction | pedestrain crossing junction with traffic light | daylight, clear sky | 108 | 0.73 | [Link](https://fordatis.fraunhofer.de/retrieve/d52be3ea-35b7-4eb3-86c3-c98f2d266f6f/INFRA-3DRC_scene-13.zip) |
| scene_14 | Two cars moving behind each other in same lane | multi-lane bidirectional straight road | twilight, clear sky | 97 | 0.67 | [Link](https://fordatis.fraunhofer.de/retrieve/8146f45d-29b9-4997-92fe-e341efd1d39c/INFRA-3DRC_scene-14.zip) |
| scene_15 | four cars moving in two lanes in the same direction| multi-lane bidirectional straight road | twilight, clear sky | 94 | 0.67 | [Link](https://fordatis.fraunhofer.de/retrieve/20603daa-2cae-4936-9f89-5df48b58cfa5/INFRA-3DRC_scene-15.zip) |
| scene_16 | one car moving | multi-lane bidirectional straight road | twilight, clear sky | 83 | 0.55 | [Link](https://fordatis.fraunhofer.de/retrieve/ccc628f9-851f-4be6-9519-bd56e2edf097/INFRA-3DRC_scene-16.zip) |
| scene_17 | one bus moving | multi-lane bidirectional straight road | twilight, clear sky  | 42 | 0.3 | [Link](https://fordatis.fraunhofer.de/retrieve/b316880f-8074-4861-8a12-5d79563b7c09/INFRA-3DRC_scene-17.zip) |
| scene_18 | One bus and two cars moving in opposite lanes | multi-lane bidirectional straight road | twilight, clear sky | 137 | 0.93 | [Link](https://fordatis.fraunhofer.de/retrieve/adcf1dda-94ab-43b8-bce9-616fdc2fd7c0/INFRA-3DRC_scene-18.zip) |
| scene_19 | One adult and one bicycle moving | open parking | daylight, clear sky | 108 | 0.82 | [Link](https://fordatis.fraunhofer.de/retrieve/ae6027cc-0fc3-45fb-afc7-532634b3bf36/INFRA-3DRC_scene-19.zip) |
| scene_20 | One adult crosses the road, one car drives towards crossing and stops | open parking |  daylight, clear sky | 89 | 0.67 | [Link](https://fordatis.fraunhofer.de/retrieve/6b3fd5a9-8916-4f03-ac28-0ddf3b602e37/INFRA-3DRC_scene-20.zip) |
| scene_21 | One bicycle crossing the road, one car drives towards crossing, waits for some time and then drives. | open parking |  daylight, clear sky | 101 | 0.75 | [Link](https://fordatis.fraunhofer.de/retrieve/21634f38-a818-4ad9-82d9-d273f926b5b7/INFRA-3DRC_scene-21.zip) |
| scene_22 | Two buses and two cars moving on the road in same direction | multi-lane bidirectional straight road | night, clear sky | 114 | 0.67 | [Link](https://fordatis.fraunhofer.de/retrieve/052ae154-57c2-48dc-be83-ac04e7c311fb/INFRA-3DRC_scene-22.zip) |
| scene_23 | Two cars moving in same direction | multi-lane bidirectional straight road | night, clear sky | 99 | 0.49 | [Link](https://fordatis.fraunhofer.de/retrieve/8451721d-00c9-4540-8a61-10d34f7af884/INFRA-3DRC_scene-23.zip) |
| scene_24 | One bus moving | multi-lane bidirectional straight road | night, clear sky | 118 | 0.58 | [Link](https://fordatis.fraunhofer.de/retrieve/42c8c940-cea0-4245-bad0-26ec11156a88/INFRA-3DRC_scene-24.zip) |
| scene_25 | Two cars moving in opposite directions | multi-lane bidirectional straight road | night, clear sky | 100 | 0.5 | [Link](https://fordatis.fraunhofer.de/retrieve/5bf14b70-3e2f-40cf-9e60-52b7c8167c07/INFRA-3DRC_scene-25.zip) |

### To download complete dataset (13.4 GB)- [Link](https://fordatis.fraunhofer.de/bitstream/fordatis/355/26/INFRA-3DRC-Dataset.zip) 

<span style="color:red"> ATTENTION - SOME TEMPORARY BUG FIXES IN 2 FILES OF DATASET </span>
* <span style="color:red">For scene_18 </span>, after downloading the dataset, only replace the downloaded **calibration.json** by this file - [calibration.json](/docs/fixes/calibration.json)
* <span style="color:red">For scene_20 </span>, after downloading the dataset, only replace the downloaded **scene.json** by this file - [scene.json](/docs/fixes/scene.json)
