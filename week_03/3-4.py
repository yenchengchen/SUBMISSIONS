#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 01:32:09 2021

@author: Yencheng
"""

a = int(input("Please input a integer:" ))

i = 1
j = 1

k = []
while i <= a or j <= a:
    if j <= a:
        #print(j)
        k.extend([j])

    if i <= a:
        #print (i)
        k.extend([i])
    
    
    j = j + i
    i = j + i
    
print(k)