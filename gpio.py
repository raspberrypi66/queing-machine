#! /usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

butPin = 17 # Broadcom pin 17 (P1 pin 11)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

bState=0#button release

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin)== 0 : # button is pressed
         if(bState ==0):#check button state  
	 	print("Button press") 
         	bState=1
         time.sleep(0.5)
        else:
         if(bState ==1 ):
                print("Button release")
                bState=0
         time.sleep(0.075)
               
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
