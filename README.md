# DDD (Diverse Driving Dataset) - Driving in Diverse Environments - A Multimodal Datasets for Contextual Driving Anomaly Analysis
Distracted drivers are more prone to overlooking potential hazards, resulting in car accidents. Consequently, detecting anomalies in driving behavior is critical to minimizing driver-related accidents, known as anomalies. The challenge lies in the many possible anomalous actions a driver can take in realistic driving under diverse driving conditions. We present a new multi-modal senor-based benchmark, the Diverse Driving Dataset (DDD) dataset, which captures data using several devices: video data using Nexar Dash pro cam, IMU, and GPS sensor data from smartphone mounted on the dashboard, physiological traits using Empatica E4 wristband, and head orientation using self-designed wearable. Such a rich dataset might help in predicting various aspects of driving- (a) driving maneuvers (through GPS, IMU), (b) drivers' attentiveness (through camera, earabale), (c) drivers' physiological parameters (through medical grade smart band), (d) driving context and environment (through the camera, IMU). We provide annotations for normal and anomalous instances based on the rear view of the dashcam, along with contextual reasons for detected anomalies such as speed, heart rate, and acceleration. Using this setup, we collected a dataset of over 48 driving sessions covering 1440 mins, each 30 minutes duration, over 5 different geographical locations covering 2 countries, India and Australia. We present our data collection set up with all the sensor devices.


<p align="center">
      <img src="DDD/DDD_setup/DataCollection.png" width="90%"/><br><strong>Fig.1:</strong> Data Collection setup while driving with 4 sensor devices worn and used by the driver.
</p>

## Dataset Description
The DDD code repository includes two folders for the two countries- India and Australia. Each country folder consists of a list of folders with names D1, D2, D3, and so on, corresponding to each trip, India with 42 trips and Australia with 6 trips. Each folder corresponding to drivers contains a list of subfolders named Smartphonesense, Wristband, Video_Data, Earable, and Annotations. However, driver’s data in Australia does not contain Earable and Samrtphonesense folders because of the unavailability of resources, such as developed Earable in Australia and the smartphone lacked internet connection to capture required data. Each folder contains files containing the data collected from the respective devices. The details about all the devices, their collected fields, sampling frequency, and file format are shown in Table 2. Smartphone-based
sensor data was collected from the developed application Safe Drive and stored collectively in sensor.csv with various fields listed in Table 2. Some of the driver's data in India does not contain smartphone sense data due to loss of connectivity. However, we record IMU data using the Nexar Dash Pro cam, stored in the sensor.txt files.  Wristband wearable sensor data leverages the CSV file format for individual sensor-based fields listed. Video of front and rear view is stored as “videoB.mp4" and
“videoA.mp4", respectively, each video of duration 1 minutes. Earable sensed data is stored as an earable.csv file with all the captured fields. Metadata, such as annotations about anomalous or normal instances and their context, are provided as annotations.csv files. Each folder corresponds to a single trip of a driver for 30 mins of continuous driving in a naturalistic setup. The folder contains subfolder video, which contains the front (driver view) and rear (on-road view) of the dashcam; sensor.csv, which contains IMU, GPS, and a few other sensor data captured using the mounted smartphone; earable.csv, which captures IMU for head movement of the driver, E4.zip which contains HR.csv,BVP.csv,IBI.csv,EDA.csv,TEMP.csv,ACC.csv and annotations.csv which contains the field of normal or anomalous instance and context field for those anomalies.


In the dataset we have given comprehensive metadata for all the sensors and their placemant. The collected attributes from each sensor is as shown below.

| `Parameters` | `Description`                                                                                |
|------------|--------------------------------------------------------------------------------------------|
| ts         | Timestamp (yyyy/mm/dd HH:MM:SS) from the ESP32 MCU after reading sensor values             |
| T          | Temperature reading of the indoor environment in celsius at time ts                        |
| H          | Humidity reading of the indoor environment in percentage at time ts                        |
| PMS1       | Less than 1 micron dust particle readings in parts per million (ppm) at time ts            |
| PMS2_5     | Less than 2.5 micron dust particle readings in ppm at time ts                              |
| PMS10      | Less than 10 micron dust particle readings in ppm at time ts                               |
| CO2        | Carbon dioxide concentration in ppm at time ts                                             |
| NO2        | Nitrogen dioxide concentration in ppm at time ts                                           |
| CO         | Carbon monoxide concentration in ppm at time ts                                            |
| VoC        | Volatile organic compounds concentration in parts per billion (ppb) at time ts             |
| C2H5OH     | Ethyl alcohol concentration in ppb at time ts                                              |
| ID         | Unique identifier of the deployed \ourmethod{} sensor                                      |
| Loc        | Location of DALTON sensor in the indoor environment                                        |
| Customer   | The name of the occupant who participated during the sensor deployment in his indoor space |
| Ph         | Phone number of the customer for urgent contact. Replaced with XXXX to preserve privacy    |


## Directory Structure
```
DDD
└── datasets
    └── India
        └── D1.zip-D2.zip-D3.zip-----D42.zip
            └── Wristband
            └── Smartphonesense (Absent for some cases due to connectivity issue)
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
    └── accuracy_computation.py
    └── model.py
└── requirements.txt
└── README.md
LICENSE
```

## Installation:

To install use the following commands.
```bash
git clone https://github.com/SugandhPargal/DDD.git
pip install -r requirements.txt
mkdir datasets
cd datasets
```

Please download the dataset through [Google Drive](https://drive.google.com/drive/folders/1G96mcICCKixY2qjKHkemLcpLBJ7ooZJ9?usp=drive_link) and paste the data in datasets directory.
# Reference
To refer the DDD Datsset, please cite the following work.

BibTex Reference:
```
@article{to_be_declared,
  title={Driving in Diverse Environments - A Multimodal Datasets for Contextual Driving Anomaly Analysis},
  author={Pargal, Sugandh and Chakraborty, Sandip},
  year={2024}
}
```
For questions and general feedback, contact [Sugandh Pargal](https://sugandhpargal.github.io/sugandh20/).
