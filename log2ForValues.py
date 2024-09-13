# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:03:04 2024

@author: Bachs
"""
import math

x = math.log2(5)
const = math.log2(2)-math.log2(3)
i=1
count = 0
last = 0
while(i<100000000):
    build = i*x+const
    if(math.ceil(build)-build<0.0000005):
        print(build)
        last=build
        count+=1
        #print(build,i)
        
    i+=1
print("Count: ",count)