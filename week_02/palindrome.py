#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:04:16 2021

@author: Yencheng
"""

name = str(input("your name?",))

i = 0
newname = ""
newname = newname + name[len(name)-1].upper()

while i <  len(name)-1:
    
    
    newname = newname + name[len(name)-i-2].lower() 
    
    i += 1
    
# palindrome check

''''

namefor = newname
namefor = namefor + name[0].lower()

i = 1
while i < len(name)-1:
    
    namefor = namefor + name[i].lower()
    
    i += 1
    
    
namerev = ""
namerev = name
namerev = namerev + name[0].lower()

i = 1
while i < len(name)-1:
    
    namefor = namefor + name[i].lower()
    
    i += 1


if namefor == namerev:
    print("Palindrome!")


else:     
    
    print(newname)
