# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:23:48 2024

@author: Bachs
"""
import math
def drop(pow5,pow2):
    numerator = pow2-pow5
    denominator = 3*pow5-3*(2**math.ceil(math.log2(pow5)))
    return(numerator/denominator)

pow5 = 5
pow2=2
try:
    with open("C:\\Users\\Bachs\\Plotting Nollatz\\PlottingNollatzTimed.txt", "w") as file:
        for i in range(1,100000):
            x = drop(pow5,pow2)
            pow5*=5
            pow2*=2
            stringy = f"({i},{x})\n"
            file.write(stringy)
        file.flush()
        print("Yippee!")
except Exception as e:
    print(f"An error occurred: {e}")