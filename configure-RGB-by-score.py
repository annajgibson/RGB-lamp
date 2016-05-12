# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: A Gibson
Date: April 2016
Write RGB to Edison Pins

"""

#import mraa library for controlling pins
import mraa
import numpy as np

# define pin numbers (there will be three LEDs with each R,G,B wired to same pin)
redLedPin = 5
greenLedPin = 6
blueLedPin = 9

# define leds as pwm
redLed = mraa.Pwm(redLedPin)
greenLed = mraa.Pwm(greenLedPin)
blueLed = mraa.Pwm(blueLedPin)

# set led pins to output
redLed.enable(True)
greenLed.enable(True)
blueLed.enable(True)

#start loop
#read in csv file
#default data type = float
while True:
    value = np.loadtxt("C:\Users\Anna\Documents\GitHub\RGB-lamp\sentiment.txt")
    #print sentiment value to console
    print(value)   
    
#check for tweet sentiment value
    #if bad sentiment
    if value < 0.3:
        redLed = 0.3
        greenLed = 0.3
        blueLed = 0.3
    #neutral sentiment
    if if value >= 0.3 and value < 0.6:
        redLed = 0.3
        greenLed = 0.3
        blueLed = 0.3  
    #good sentiment
    if value >= 0.6 and value <= 1:
        redLed = 0.3
        greenLed = 0.3
        blueLed = 0.3
        #no sentiment read
        #no sentiment read
    elif  0 <= value <= 1:
        print ("bad value")
        redLed = 0
        greenLed = 0
        blueLed = 0
#how to write to LED??

