#! /usr/bin/env python3
# coding: utf-8
import os
import time
import sys
import serial

rotationDegree = 10
fullCycleRound = 0
print ("\n=========", "Stingray RF Test script", "=========" )
ser = serial.Serial ('COM1', 9600, timeout = 1) # open configured seiral port

if ser.is_open == True:
    print ("\nserial port is openned\n")
    while rotationDegree <= 360 :
        print ("rotation angle is now", rotationDegree)
        ser.write(b'Step CW\r\n')  # write serial command to turntable
        time.sleep(11)             # wait at least 11 sec to execute next command
        rotationDegree += 10
        s = ser.read(10)
        s = s.decode()
        print (s)
    if rotationDegree > 360 :
        fullCycleRound += 1
        print ("\nrotation cycle is now",fullCycleRound)
else :
    ser.close()
    if ser.is_open == False:
        print ("\nserial port is closed\n")
print ("\n=========", "End of Test", "=========\n" )
exit()