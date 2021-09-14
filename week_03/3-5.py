#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:26:55 2021

@author: Yencheng
"""

a = int(input("Enter a row number "))

pascal = [[0 for i in range(a)] for j in range(a)]

for i in range(a):
    for j in range(a):
        if i == j:
            pascal[i][j] = 1
            
            
        elif j == 0:
            pascal[i][j] =1
            
            
        else:
            
            pascal[i][j] = pascal[i -1][j] + pascal[i-1][j-1]
            
for i in range(a):
    print(pascal[a-1][i], end = " ")