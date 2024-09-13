# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:53:13 2024

@author: Bachs
"""

def greedyDrop(length, last):
    total=0
    for i in range(0, length):
        total+=(-5**(length-i-1))*2**(i)
    total/=((5**length)-2**(last+length-1))
    return total

try:
    with open("C:\\Users\\Bachs\\Plotting Nollatz\\JustSomePoints.txt", "w") as file:
        last = 1
        total = 0
        for length in range(1, 100):
            while (total := greedyDrop(length, last)) < 0:
                last += 1
            stringy = f"({length},{total}),{last}\n"
            file.write(stringy)
        file.flush()
        print("File written successfully.")
except Exception as e:
    print(f"An error occurred: {e}")