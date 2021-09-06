#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:04:06 2021

@author: Yencheng
"""
import math

a = float(input("please input a:",))
b = float(input("please input b:",))

c = float(input("please input 1,2 or 3 for: 1. arithmetic meam. \
                2. geometric mean. 3. root-mean-square",))
                

if c == 1:
    output = (a+b)/2
    
elif c == 2:
        
    output = math.sqrt(a+b)
        
elif c == 3:
    
    output = math.sqrt((a**2+b**2)/2)
    
    
    
print(output)