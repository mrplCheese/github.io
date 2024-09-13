# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 23:42:44 2024

@author: Bachs
"""

import matplotlib.pyplot as plt
import math
import plotly.tools as tls
import plotly.io as pio
import os
# Step 1: Read the file and extract coordinates
x_coords = []
y_coords = []

with open("C:\\Users\\Bachs\\Plotting Nollatz\\TimedPlotting.txt", 'r') as file:  # Replace 'coordinates.txt' with the path to your file
    for line in file:
        # Remove any surrounding whitespace and parentheses, then split by comma
        coord = line.strip().strip('()').split(',')
        x_coords.append(float(coord[0]))
        y_coords.append(float(coord[1]))
        #if(float(coord[1])-math.floor(float(coord[1]))<0.0001):
        #    print(coord[1])
        #print("AAA")
# Step 2: Plot the coordinates

#plt.scatter(x_coords, y_coords)
#plt.xlabel('dimension')
#plt.ylabel('dropKick')
#plt.title('Greedy Drops!!!')
#plt.show()

# Step 2: Create a figure and plot the coordinates
fig, ax = plt.subplots()  # Create a figure object
ax.scatter(x_coords, y_coords)
ax.set_xlabel('dimension')
ax.set_ylabel('dropKick')
ax.set_title('Greedy Drops!!!')

# Ensure the figure is drawn (so the canvas is created)
fig.canvas.draw()


#plotly_version = tls.mpl_to_plotly(fig)
#pio.write_html(plotly_version, "C:\\Users\\Bachs\\Plotting Nollatz")
# Manually creating the file and writing HTML content
# Create directory if it doesn't exist
#directory = "C:\\Users\\Bachs\\Plotting Nollatz"
#if not os.path.exists(directory):
#    os.makedirs(directory)

# Manually create the file and write the HTML content using utf-8 encoding
#with open(os.path.join(directory, 'interactive_plot.html'), 'w', encoding='utf-8') as f:
#    html_content = pio.to_html(plotly_version, full_html=True)
#    f.write(html_content)