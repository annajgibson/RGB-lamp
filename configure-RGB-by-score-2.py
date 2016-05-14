# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: A Gibson
Date: April 2016
Write RGB to Edison Pins

"""

#import mraa library for controlling pins
import mraa

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
    f = open("sentiment.txt", 'r')
    value = float(f.read())
    #print sentiment value to console
    print(value)   
    
#check for tweet sentiment value
    #if bad sentiment
    if value < 0.3:
        redLed.write(0)
        greenLed.write(1)
        blueLed.write(1)
    #neutral sentiment
    elif value >= 0.3 and value < 0.6:
        redLed.write(1)
        greenLed.write(0)
        blueLed.write(1)  
    #good sentiment
    elif value >= 0.6 and value <= 1:
        redLed.write(1)
        greenLed.write(1)
        blueLed.write(0)
        #no sentiment read
        #no sentiment read
    elif value < 0 or value > 1:
        #print ("bad value")
        redLed.write(0)
        greenLed.write(0)
        blueLed.write(0)


