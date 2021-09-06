#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:59:03 2021

@author: Yencheng
"""

price = float(input("Enter the price of a meal: "))


tip = price * 0.16
total = price + tip

print("A 16% tip would be:", "{:.2f}".format(tip))
print("The total including tip would be:", "{:.2f}".format(total))