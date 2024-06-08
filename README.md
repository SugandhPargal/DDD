# DDD (Diverse Driving Dataset) - Driving in Diverse Environments - A Multimodal Datasets for Contextual Driving Anomaly Analysis
Distracted drivers are more prone to overlooking potential hazards, resulting in car accidents. Consequently, detecting anomalies in driving behavior is critical to minimizing driver-related accidents, known as anomalies. The challenge lies in the many possible anomalous actions a driver can take in realistic driving under diverse driving conditions. We present a new multi-modal senor-based benchmark, the Diverse Driving Dataset (DDD) dataset, which captures data using several devices: video data using Nexar Dash pro cam, IMU, and GPS sensor data from smartphone mounted on the dashboard, physiological traits using Empatica E4 wristband, and head orientation using self-designed wearable. Such a rich dataset might help in predicting various aspects of driving- (a) driving maneuvers (through GPS, IMU), (b) drivers' attentiveness (through camera, earabale), (c) drivers' physiological parameters (through medical grade smart band), (d) driving context and environment (through the camera, IMU). We provide annotations for normal and anomalous instances based on the rear view of the dashcam, along with contextual reasons for detected anomalies such as speed, heart rate, and acceleration. Using this setup, we collected a dataset of over 48 driving sessions covering 1440 mins, each 30 minutes duration, over 5 different geographical locations covering 2 countries, India and Australia. 


## Dataset Description
The DDD code repository includes two folders for the two countries- India and Australia. Each country folder consists of a list of folders with names D1, D2, D3, and so on, corresponding to each trip, India with 42 trips and Australia with 6 trips. Each folder corresponding to drivers contains a list of subfolders named Smartphonesense, Wristband, Video_Data, Earable, and Annotations. However, driver’s data in Australia does not contain Earable and Samrtphonesense folders because of the unavailability of resources, such as developed Earable in Australia and the smartphone lacked internet connection to capture required data. Each folder contains files containing the data collected from the respective devices. The details about all the devices, their collected fields, sampling frequency, and file format are shown in Table 2. Smartphone-based
sensor data was collected from the developed application Safe Drive and stored collectively in sensor.csv with various fields listed in Table 2. Some of the driver's data in India does not contain smartphone sense data due to loss of connectivity. However, we record IMU data using the Nexar Dash Pro cam, stored in the sensor.txt files.  Wristband wearable sensor data leverages the CSV file format for individual sensor-based fields listed. Video of front and rear view is stored as “videoB.mp4" and
“videoA.mp4", respectively, each video of duration 1 minutes. Earable sensed data is stored as an earable.csv file with all the captured fields. Metadata, such as annotations about anomalous or normal instances and their context, are provided as annotations.csv files. Each folder corresponds to a single trip of a driver for 30 mins of continuous driving in a naturalistic setup. The folder contains subfolder video, which contains the front (driver view) and rear (on-road view) of the dashcam; sensor.csv, which contains IMU, GPS, and a few other sensor data captured using the mounted smartphone; earable.csv, which captures IMU for head movement of the driver, E4.zip which contains HR.csv,BVP.csv,IBI.csv,EDA.csv,TEMP.csv,ACC.csv and annotations.csv which contains the field of normal or anomalous instance and context field for those anomalies.

## Directory Structure
India
 D1
  Earable
  Smartphonesense
  Video_Data
  Wristband
     
$ tree
.
├── dir1
│   ├── file11.ext
│   └── file12.ext
├── dir2
│   ├── file21.ext
│   ├── file22.ext
│   └── file23.ext
├── dir3
├── file_in_root.ext
└── README.md

3 directories, 7 files
