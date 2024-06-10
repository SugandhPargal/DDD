# DDD (Diverse Driving Dataset) 
Distracted drivers are more prone to overlooking potential hazards, resulting in car accidents. Consequently, detecting anomalies in driving behavior is critical to minimizing driver-related accidents, known as anomalies. The challenge lies in the many possible anomalous actions a driver can take in realistic driving under diverse driving conditions. We present a new multi-modal senor-based benchmark, the Diverse Driving Dataset (DDD) dataset, which captures data using several devices: video data using Nexar Dash pro cam, IMU, and GPS sensor data from smartphone mounted on the dashboard, physiological traits using Empatica E4 wristband, and head orientation using self-designed wearable. Such a rich dataset might help in predicting various aspects of driving- (a) driving maneuvers (through GPS, IMU), (b) drivers' attentiveness (through camera, earabale), (c) drivers' physiological parameters (through medical grade smart band), (d) driving context and environment (through the camera, IMU). We provide annotations for normal and anomalous instances based on the rear view of the dashcam, along with contextual reasons for detected anomalies such as speed, heart rate, and acceleration. Using this setup, we collected a dataset of over 48 driving sessions covering 1440 mins, each 30 minutes duration, over 5 different geographical locations covering 2 countries, India and Australia. We present our data collection set up with all the sensor devices.


<p align="center">
      <img src="DDD_setup/DataCollection.png" width="60%"/><br><strong>Fig.1:</strong> Data Collection setup while driving with 4 sensor devices worn and used by the driver.
</p>

## Dataset Description
The DDD code repository includes two folders for the two countries- India and Australia. Each country folder consists of a list of folders with names D1, D2, D3, and so on, corresponding to each trip, India with 42 trips and Australia with 6 trips. Each folder corresponding to drivers contains a list of subfolders named Smartphonesense, Wristband, Video_Data, Earable, and Annotations. However, driver’s data in Australia does not contain Earable and Samrtphonesense folders because of the unavailability of resources, such as developed Earable in Australia and the smartphone lacked internet connection to capture required data. Each folder contains files containing the data collected from the respective devices. The details about all the devices, their collected fields, sampling frequency, and file format are shown in Table 2. Smartphone-based
sensor data was collected from the developed application Safe Drive and stored collectively in sensor.csv with various fields listed in Table 2. Some of the driver's data in India does not contain smartphone sense data due to loss of connectivity. However, we record IMU data using the Nexar Dash Pro cam, stored in the sensor.txt files.  Wristband wearable sensor data leverages the CSV file format for individual sensor-based fields listed. Video of front and rear view is stored as “videoB.mp4" and
“videoA.mp4", respectively, each video of duration 1 minutes. Earable sensed data is stored as an earable.csv file with all the captured fields. Metadata, such as annotations about anomalous or normal instances and their context, are provided as annotations.csv files. Each folder corresponds to a single trip of a driver for 30 mins of continuous driving in a naturalistic setup. The folder contains subfolder video, which contains the front (driver view) and rear (on-road view) of the dashcam; sensor.csv, which contains IMU, GPS, and a few other sensor data captured using the mounted smartphone; earable.csv, which captures IMU for head movement of the driver, E4.zip which contains HR.csv,BVP.csv,IBI.csv,EDA.csv,TEMP.csv,ACC.csv and annotations.csv which contains the field of normal or anomalous instance and context field for those anomalies.


We have given comprehensive metadata for all the sensors and their placement in the dataset. The collected attributes from each sensor is as shown below.

| `Device`                  | `Fields`                      | `Sampling Frequency (Hz)`|   `Storage`      |
|---------------------------|-------------------------------|--------------------------|------------------|
| Smartphone (SafeDrive App)|Accelerometer -x,y,z           |                          |                  |
|                           |Gyroscope- x,y,z               |                          |                  |
|                           |Gravity- x,y,z                 |                          |                  |
|                           |Linear Acceleration            |            120           |  sensor.csv      |
|                           |Magnetometer- x,y,z            |                          |                  |
|                           |Orientation- x,y,z             |                          |                  |
|                           |GPS- Latitude, Longitude       |                          |                  |
|                           |Speed                          |                          |                  |
| Empatica E4 Wristband     |Electrodermal Activity (EDA)   |             4            |   EDA.csv        |
|                           |Blood Volume Pulse (BVP)       |             64           |   BVP.csv        |
|                           |Inter-beat Interval (IBI)      |             -            |   IBI.csv        |
|                           |Heart Rate Variability (HRV)   |             1            |   HR.csv         |
|                           |Accelerometer -x,y,z           |             32           |   ACC.csv        |
|                           |Temperature                    |             4            |   TEMP.csv       |
| Nexar Dash Pro Cam (Front)|Video (1280x720)               |             30 fps       |   videoB.mp4     |
| Nexar Dash Pro Cam (Rear) |Video (1280x720)               |             30 fps       |   videoA.mp4     |
| Custom Earable Device     |Accelerometer - x,y,z          |             40           |   earable.csv    |
|                           |Gyroscope - x,y,z              |             40           |   earable.csv    |
|Annotations                |Instance, Context              |             1per 30s     |  annotations.csv |

All the files have the first column as Timestamp (yyyy/mm/dd HH:MM:SS) recorded as Epoch & Unix Timestamp.







   





## Directory Structure
```
DDD
└── datasets
    └── India
        └── D1.zip-D2.zip-D3.zip-----D42.zip
            └── Wristband
            └── Smartphonesense (Absent in some cases due to connectivity issues)
            └── Video_Data
            └── Earable
            └── Annotations
    └── Australia
        └── D43.zip-D44.zip-D45.zip-----D48.zip
            └── Wristband
            └── Video_Data
            └── Annotations
└── codebase
    └── data_preprocessing.py
    └── merge_wristband.py
    └── model.py
    └── accuracy_computation.py
└── requirements.txt
└── README.md
LICENSE
```

## Installation:

To install use the following commands.
```bash
git clone https://github.com/SugandhPargal/DDD.git
pip install -r requirements.txt
cd datasets
```

Please download the dataset through [Google Drive](https://drive.google.com/drive/folders/1G96mcICCKixY2qjKHkemLcpLBJ7ooZJ9?usp=drive_link) and paste the data in datasets directory.
# Reference
To refer the DDD Datsset, please cite the following work.

BibTex Reference:
```
TO BE DECLARED
```
For questions and general feedback, contact [Sugandh Pargal](https://sugandhpargal.github.io/sugandh20/).
