# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:28:29 2021

@author: Akshay
"""

import pandas as pd
import matplotlib.pyplot as plt
import Lab3Functions as l3f
import EMGfunctions as emgf


coulumn_names = ['emg','t']

weights,mvc, faigue = l3f.import_data(',')

plt.figure()
plt.plot(mvc.t,mvc.emg)

emg = mvc.emg
time = mvc.t/1000

emgcorrectmean = emgf.remove_mean(emg,time)
emgfiltered = emgf.emg_filter(emgcorrectmean, time)
remgrectified = emgf.emg_rectify(emgfiltered, time)

emg_filtered, emg_rectified  = emgf.altogether(time, emgcorrectmean,low_pass = 2, sfreq = 1000, high_band = 20,low_band = 450)
