#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 14:31:25 2021

@author: Yencheng
"""

name = input("Enter your name:",)

x = name.split()


fullname = []
new = ""
for i in range(len(x)):
#    print(x[i])

  
    new = "A"
    
    j = 1
    while j < len(x[i]):
        new = new + x[i][j].lower()
        
        j += 1
        
    new = new + x[i][0].lower() + "ay"   
        
    
    fullname.append(new)
    
if len(x) == 3:  
    
    print(fullname[0]+ " " + fullname[1]+ " " + fullname[2])
    
    
elif len(x) == 2:
    print(fullname[0]+ " " + fullname[1])
    

elif len(x) == 1:
    print(fullname[0])
    


