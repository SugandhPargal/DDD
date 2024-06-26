# -*- coding: utf-8 -*-
"""preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sP0GZWJlrvVX6ziW1-SLr92uocfPH8ms

Specify the filename and the the fields present in each file name to be processed.
"""

import pandas as pd
import matplotlib.pyplot as plt
import csv
df = pd.read_csv('file_name.csv', sep=',',names=['Timestamp', 'ACCx', 'ACCy','Accz','Gyrox','Gyroy','Gyroz'])

df

pd.to_datetime(df['Timestamp'])

"""This will tell you in which range of low and high cutoff you require the frequencies based on your dataset. In our case, it is in range 0.5-2 Hz."""

import numpy as np
from numpy.fft import fft, ifft

X = fft(df['Gyroz'])
N = len(X)
n = np.arange(N)
T = N/44
freq = n/T

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0,None)
plt.ylim(-1,100)
plt.subplot(122)
plt.plot(ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
def butter_bandpass(lowcut, highcut, fs, order=5):
   nyq = 0.5 * fs
   low = lowcut / nyq
   high = highcut / nyq
   b, a = butter(order, [low, high], btype='band')
   return b, a
def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
   b, a = butter_bandpass(lowcut, highcut, fs, order=order)
   y = filtfilt(b, a, data)
   return y
fs = 44

order = 4
filtered = butter_bandpass_filter(df2['ACCx'], 0.5, 2, fs, order)
print("The length of frequencies:",len(filtered))
print("The Butterworth bandpass filter output of first 50 frequencies:",filtered)
plt.clf()
fig, ax = plt.subplots()
ax.plot(df2['ACCx'].values, label='Original signal')
ax.plot(filtered, label='Filtered signal')
plt.xlim(0,1000)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()

"""Normalizing Raw Data"""

from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
# load the dataset and print the first 5 rows
#series = read_csv('daily-minimum-temperatures-in-me.csv', header=0, index_col=0)
#print(series.head())
# prepare data for normalization
values = filtered
fig, ax = plt.subplots()
ax.plot(filtered, label='Filtered signal')
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
normalized = scaler.transform(values)
print(normalized)
df2['normalized_ACCy'] = normalized
print(df2['normalized_ACCy'] )
print(filtered)
fig, ax = plt.subplots()
ax.plot(normalized, label='normalised')
ax.plot(filtered, label='Filtered signal')
plt.xlim(0,None)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
