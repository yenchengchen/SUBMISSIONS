#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 01:32:09 2021

@author: Yencheng
"""

a = int(input("Please input a integer:" ))

i = 1
j = 1
while i <= a or j <= a:
    if j <= a:
        print(j)

    if i <= a:
        print (i)
    
    
    j = j + i
    i = j + i