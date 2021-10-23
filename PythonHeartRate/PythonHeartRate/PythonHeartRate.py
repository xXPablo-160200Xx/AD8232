import serial
import numpy as np
import time
from scipy.signal import find_peaks

Time = time.gmtime()
Seg0 = Time[5]
Flag0 = Time[5]
Port = serial.Serial('COM3', baudrate = 9600)#,timeout = 2)

Data = []

if Seg0<=45:
    Seg1 = Seg0+15
    while Seg0<Seg1:
        arduinoread = Port.readline().decode('ascii')
        arduinoread = arduinoread.rstrip()
        print(arduinoread.rstrip())
        #arduinoread=1
        Data.append(int(arduinoread))
        Seg0 = time.gmtime()[5]
        print(Seg0)
        #N+=1
else:
    Seg1 = 15-(60-Seg0)
    while Seg1!=Seg0:
        arduinoread = Port.readline().decode('ascii')
        arduinoread = arduinoread.rstrip()
        print(arduinoread.rstrip())
        #arduinoread=0
        Data.append(int(arduinoread))
        Seg0 = time.gmtime()[5]
        print(Seg0)
        #N+=1

print(Data,Flag0,Seg1,'Flag0')
Data = np.array(Data)
np.savetxt('D:\\OneDrive - Fundacion Universidad de las Americas Puebla\\UDLAP\\9no_SEMESTRE\\SERVICIO SOCIAL\\CODES\\HEART\\HEART\\HeartData.csv', Data, delimiter = ',')

