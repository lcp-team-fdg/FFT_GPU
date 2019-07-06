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
import json 


'''
For each set of style and range settings, plot n random points in the box
    latitude is the x-axis from range [0, 90] decimal degrees
    longitude is the y-axis from range [0, 180] decimal degrees
    amplitude is the z axis from range [0, 10] integer 
'''
# Define Arrays from File 
array1Max = 3.00
array1Min = 0.00 

array2Max = 3.00
array2Min = 0.00 

array3Max = 3.00
array3Min = 0.00 

array4Max = 3.00
array4Min = 0.00 


amplitudeZAxis = []
latitudeXAxis = []
longitudeYAxis = []

amplitudeGreaterTen = []
amplitudeGreaterEight = []
amplitudeGreaterSix = []
amplitudeGreaterFour = []

latitudeGreaterTen = []
latitudeGreaterEight = []
latitudeGreaterSix = []
latitudeGreaterFour = []

longitudeGreaterTen = []
longitudeGreaterEight = []
longitudeGreaterSix = []
longitudeGreaterFour = []

#ax.scatter(latitudeXAxis, longitudeYAxis, amplitudeGreaterTen, c=color, marker=symbol)
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
Read from file
'''
#TODO OPEN DATABASE AND READ IT.

with open('','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
	
    #define the symbol to plot (each array can also have their own)
    symbol = ('o')
    
    #for i in amplitudeZAxis:
    for row in plots:  
     
        # Array for IED Detection anything greater than 10 - Red 
        if float(row[0]) > 10.00 :
            amplitudeGreaterTen.append(float(row[0]))
            latitudeGreaterTen.append(float(row[1]))
            longitudeGreaterTen.append(float(row[2]))
            symbol = ('o')
            
        # Array for IED Detection anything greater than 8 and less than 9.99 - black
        elif float(row[0]) > 8.00 and float(row[0]) < 9.99 :
            amplitudeGreaterEight.append(float(row[0]))
            latitudeGreaterEight.append(float(row[1]))
            longitudeGreaterEight.append(float(row[2]))
			
        # Array for IED Detection anything greater than 6 and less than 7.99 - gray
        elif float(row[0]) > 6.00 and float(row[0]) < 7.99 :
            amplitudeGreaterSix.append(float(row[0]))
            latitudeGreaterSix.append(float(row[1]))
            longitudeGreaterSix.append(float(row[2]))

        # Array for IED Detection anything less than 5.99 - silver 
        elif float(row[0]) < 5.99 :
            amplitudeGreaterFour.append(float(row[0]))
            latitudeGreaterFour.append(float(row[1]))
            longitudeGreaterFour.append(float(row[2]))
   

# Scatter Plot (lat, long, snr, color, symbol) - red, silver, gray and black          
ax.scatter(latitudeGreaterFour, longitudeGreaterFour, amplitudeGreaterFour, c=["silver"], marker=symbol)
ax.scatter(latitudeGreaterSix, longitudeGreaterSix, amplitudeGreaterSix, c=["gray"], marker=symbol)
ax.scatter(latitudeGreaterEight, longitudeGreaterEight, amplitudeGreaterEight, c=["black"], marker=symbol)	
ax.scatter(latitudeGreaterTen, longitudeGreaterTen, amplitudeGreaterTen, c=["red"], marker=symbol)
      
# pause the plot for a few seconds
plt.pause(10)
	  
# Show the plot 				
plt.show()
csvfile.close()