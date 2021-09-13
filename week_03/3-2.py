#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 23:53:31 2021

@author: Yencheng
"""

matrix = input("Please input 4 numbers:",)

x = matrix.split()

a = float(x[0])
b = float(x[1])
c = float(x[2])
d = float(x[3])

k = a*d-b*c

ai = d/k
bi = -b/k
ci = -c/k
di = a/k

print(f"matrix: (({a:.4f}, {b:.4f}), ({c:.4f}, {d:.4f}))")
print(f"inverse: (({ai:.4f}, {bi:.4f}), ({ci:.4f}, {di:.4f}))")