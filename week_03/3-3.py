#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 00:28:58 2021

@author: Yencheng
"""

dict = {"Sunday":[], "Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[],\
       "Friday":[], "Saturday":[]}
    
#print("Monday"in dict)


while True :
    do = input("what do you want to do?")
    
    
    
    if do == "add":
        
        whatday = input("What day?")
        
        if whatday in dict:
        
            todo = input("What would you like to add at " + whatday +"?")
        
            dict[whatday].extend([todo])
            
        else:
            print("Invalid entry - please enter a correct day of the week \
(like Monday, Tuesday...)")
        
       
    elif do == "get":
        
        get = input("Get what day?")
        
        for i in range(len(dict[get])):
        
            print( "You have to " + dict[get][i])
        
    elif do == "quit":
        print("Ending program. Thank you for using the to-do list!")
        break    
      
    
    else:
    
        print ("Invalid entry - please enter a correct command (add, get, or quit)")