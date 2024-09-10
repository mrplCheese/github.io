# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:42:44 2024

@author: Bachs
"""

import matplotlib.pyplot as plt
import math
# Step 1: Read the file and extract coordinates
x_coords = []
y_coords = []

with open("C:\\Users\\Bachs\\Plotting Nollatz\\TimedPlotting.txt", 'r') as file:  # Replace 'coordinates.txt' with the path to your file
    for line in file:
        # Remove any surrounding whitespace and parentheses, then split by comma
        coord = line.strip().strip('()').split(',')
        x_coords.append(float(coord[0]))
        y_coords.append(float(coord[1]))
        if(float(coord[1])-math.floor(float(coord[1]))<0.0001):
            print(coord[1])

# Step 2: Plot the coordinates
plt.scatter(x_coords, y_coords)
plt.xlabel('dimension')
plt.ylabel('dropKick')
plt.title('Greedy Drops!!!')
plt.show()