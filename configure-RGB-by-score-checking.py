# -*- coding: utf-8 -*-
"""
Program: configure-RGB-by-score-checking.py
Spyder Editor
Author: A Gibson
Date: April 2016
Write RGB to Edison Pins

"""

#testing loop
import numpy as np
#start loop
#read in csv file
#default data type = float
while True:
    value = np.loadtxt("C:\Users\Anna\Documents\GitHub\RGB-lamp\sentiment.txt")
    #print sentiment value to console
    #print(value)   
    
#check for tweet sentiment value
    #if bad sentiment
    if value < 0.3:
        print("bad sentiment") 
    #neutral sentiment
    if value >= 0.3 and value < 0.6:
        print("neutral sentiment")  
    #good sentiment
    if value >= 0.6 and value <= 1:
        print("good sentiment") 
    #no sentiment read
    elif value < 0  or value > 1:
        print ("bad value, exiting")
        break
        



