'''
================================================
 Future Defense Group (FDG)
 File used to graph the IED Detection Pattern.
================================================

'''

# Libraries
#!/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv
import socket
import sys
import json

'''
Talk to the database 
'''
from fdg.client.fdg_client import Client

cli = Client(url='http://127.0.0.1:8080', username='admin', password='password')

'''
For each set of style and range settings, plot n random points in the box
    latitude is the x-axis from range [0, 90] decimal degrees
    longitude is the y-axis from range [0, 180] decimal degrees
    amplitude is the z axis from range [0, 10] integer 
'''
# Config Data for Max/Min SNR Values for each array/color 
array1Max = 10.00

array2Max = 9.99
array2Min = 8.00 

array3Max = 7.99
array3Min = 6.00 

array4Min = 5.99

# define the x, y, z axis 
amplitudeZAxis = []
latitudeXAxis = []
longitudeYAxis = []

# define four arrays for each color we plot. 
amplitudeArray1 = []
amplitudeArray2 = []
amplitudeArray3 = []
amplitudeArray4 = []

latitudeArray1 = []
latitudeArray2 = []
latitudeArray3 = []
latitudeArray4 = []

longitudeArray1 = []
longitudeArray2 = []
longitudeArray3 = []
longitudeArray4 = []

#ax.scatter(latitudeXAxis, longitudeYAxis, amplitude, c=color, marker=symbol)
# fig.add_sub_plot(number of rows, number of columns, index of subplot)
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')

# Labels for Axis (x, y, z)
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Amplitude')

# Turn off Scientific Notation
ax.ticklabel_format(useOffset=False)

'''
Read from database
'''
#TODO OPEN DATABASE AND READ IT.
gps_obj = cli.get_gps_coordinates()
gps = gps_obj['gps']


for obj in gps : 

    obj_fields = obj['fields']
    #print(obj_fields['stat_snr'], ", ", obj_fields['telemetry']['latitude'], ", ", obj_fields['telemetry']['longitude'])
    
    # Array for IED SNR Detection anything greater than array1Max - Red 
    if float(obj_fields['stat_snr']) > array1Max :
        amplitudeArray1.append(obj_fields['stat_snr'])
        latitudeArray1.append(obj_fields['telemetry']['latitude'])
        longitudeArray1.append(obj_fields['telemetry']['longitude'])
        
    # Array for IED SNR Detection anything greater than array2Min and less than array2Max - black
    elif float(obj_fields['stat_snr']) > array2Min and float(obj_fields['stat_snr']) < array2Max :
        amplitudeArray2.append(obj_fields['stat_snr'])
        latitudeArray2.append(obj_fields['telemetry']['latitude'])
        longitudeArray2.append(obj_fields['telemetry']['longitude'])
        
    # Array for IED SNR Detection anything greater than array3Min and less than array3Max - gray
    elif float(obj_fields['stat_snr']) > array3Min and float(obj_fields['stat_snr']) < array3Max :
        amplitudeArray3.append(obj_fields['stat_snr'])
        latitudeArray3.append(obj_fields['telemetry']['latitude'])
        longitudeArray3.append(obj_fields['telemetry']['longitude'])

    # Array for IED SNR Detection anything less than array4Min - silver 
    elif float(obj_fields['stat_snr']) < array4Min :
        amplitudeArray4.append(obj_fields['stat_snr'])
        latitudeArray4.append(obj_fields['telemetry']['latitude'])
        longitudeArray4.append(obj_fields['telemetry']['longitude'])
			
#define the symbol to plot (each array can also have their own)
symbol = ('o')   

# Scatter Plot (lat, long, snr, color, symbol) - red, silver, gray and black          
ax.scatter(latitudeArray4, longitudeArray4, amplitudeArray4, c=["silver"], marker=symbol)
ax.scatter(latitudeArray3, longitudeArray3, amplitudeArray3, c=["gray"], marker=symbol)
ax.scatter(latitudeArray2, longitudeArray2, amplitudeArray2, c=["black"], marker=symbol)	
ax.scatter(latitudeArray1, longitudeArray1, amplitudeArray1, c=["red"], marker=symbol)
      
# pause the plot for a few seconds
plt.pause(3)	
  
# Show the plot 				
plt.show()
