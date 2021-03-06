# -*- coding: utf-8 -*-
"""
Spyder Editor
Author: R Winch
Date: April 2016
Write RGB to Edison Pins

"""

#import mraa library for controlling pins
import mraa

# define pin numbers
redPotPin = 0
greenPotPin = 1
bluePotPin = 2
redLedPin = 5
greenLedPin = 6
blueLedPin = 9

# define potentiometers as analog in
redPot = mraa.Aio(redPotPin)
greenPot = mraa.Aio(greenPotPin)
bluePot = mraa.Aio(bluePotPin)

# define leds as pwm
redLed = mraa.Pwm(redLedPin)
greenLed = mraa.Pwm(greenLedPin)
blueLed = mraa.Pwm(blueLedPin)

# set led pins to output
redLed.enable(True)
greenLed.enable(True)
blueLed.enable(True)

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