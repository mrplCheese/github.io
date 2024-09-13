# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 00:21:44 2024

@author: Bachs
"""

"""
Created on Fri Aug 16 00:23:48 2024

@author: Bachs
"""
import math
def drop(pow5,pow2):
    numerator = pow2-pow5
    denominator = 3*(pow5-2**math.ceil(math.log2(pow5)))
    return(numerator/denominator)

pow5=5
pow2=2
stringy=""
try:
    with open("C:\\Users\\Bachs\\Plotting Nollatz\\SomeGuyMethod.txt", "w") as file:
        for i in range(1,100001):
            x = drop(pow5,pow2)
            pow5*=5
            pow2*=2
            stringy+=f"({i},{x})\n"
            if i%1000==0:
                print(i)
                file.write(stringy)
                stringy=""
        file.flush()
        print("Yippee!")
except Exception as e:
    print(f"An error occurred: {e}")