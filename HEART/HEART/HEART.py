import heartpy as hp
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from scipy.signal import find_peaks

Time = time.gmtime()
print(Time[4])
Great = []
Red_calibration = pd.read_csv('HeartData.csv', sep=',', header=None) #In this part it only reads and changes the type of csv files that contain the calibration matrix
Red_calibration = np.array(Red_calibration, dtype=np.int16)           #Apply the same Methodology in each BGR layer.
for i,e in enumerate(Red_calibration):
    Great.append(e/1000)
    #print(Great[i])
Great = np.array(Great)
D1 = Great.flatten()
D1 = D1[:]
print(D1)
np.savetxt('Great.csv', Great, delimiter = ',')

print(Great)
print(Red_calibration)

sample_rate = 200
data = hp.get_data('Great.csv')
data = data[:]

peaks, _ = find_peaks(D1, height=0.5)
BPM = (len(peaks))*4
BPM = str(BPM)
BPM = "BPM = " + BPM

filtered = hp.filter_signal(data, cutoff = 0.05, sample_rate = sample_rate, filtertype='notch')
plt.figure(figsize=(12,4))
plt.plot(filtered[800:1000], alpha=0.5, label = 'filtered signal')
plt.legend()

plt.figure(figsize=(12,4))
plt.plot(filtered, alpha=0.5, label = 'filtered signal')
plt.legend()

plt.figure(figsize=(12,4))
plt.plot(Great[600:1000])

plt.figure(figsize=(12,4))
plt.title(BPM)
plt.plot(D1)
plt.plot(peaks, D1[peaks], "x")
plt.show()
plt.clf()



#run analysis
wd, m = hp.process(data[:], sample_rate)

#visualise in plot of custom size
plt.figure(figsize=(12,4))
hp.plotter(wd, m)
#display computed measures
for measure in m.keys():
    print('%s: %f' %(measure, m[measure]))

"""
data = hp.get_data('D:\\OneDrive - Fundacion Universidad de las Americas Puebla\\UDLAP\\9no_SEMESTRE\\SERVICIO SOCIAL\\CODES\\PythonHeartRate\\PythonHeartRate\\HeartData.csv')
working_data, measures = hp.process(data, 200.0)
hp.plotter(working_data, measures)


import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Fire in the hole!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))
"""
