#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:36:17 2021

@author: Yencheng
"""

gallon = float(input("Please input the number of gallons of gasoline:",))


liters= "{:.4f}".format(gallon * 3.78541)
barrels = "{:.3f}".format(gallon / 19.5)
price = "{:.2f}".format(gallon * 3.65)

print(liters)
print(barrels)
print(price)