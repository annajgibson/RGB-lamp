# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: A Gibson
Date: April 2016
Write RGB to Edison Pins

"""

#import mraa library for controlling pins
import mraa
import numpy


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


#check for tweet sentiment value

#loop through pins and assign RGB if


# loop forever
while 1:
	# read from pots
	redPotReading = redPot.readFloat()
	greenPotReading = greenPot.readFloat()
	bluePotReading = bluePot.readFloat()
	
	# prevent flickering when near off state
	if redPotReading > 0.97:
		redPotReading = 1
	if greenPotReading > 0.9:
		greenPotReading = 1
	if bluePotReading > 0.98:
		bluePotReading = 1	

	# write to leds		
	redLed.write(redPotReading)
	greenLed.write(greenPotReading)
	blueLed.write(bluePotReading)

	# print current readings
	print "Red: {: 0.2f} - Green {: 1.2f} - Blue {: 2.2f}".format(1 - redPotReading, 1 - greenPotReading, 1 - bluePotReading)