#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 22:25:01 2021

@author: Yencheng
"""

a = float(input("input your income:",))


if a <= 1000:
    tax = a *0.05
    
    
elif a <= 2000:
    tax = (a-1000)*0.1 + 1000*0.05
    
    
else: 
    tax = (a-2000)*0.15 + 1000*0.1 + 1000*0.05
    
    
print(tax)