#! /usr/bin/env python3
# coding: utf-8

#TO DO: 
#add command rotate clockwise and anti-clockwise
#add function to configure rotate speed and degree for each turn
#add user input to execute more cycles
#add debug mode

import os
import time
import serial

rotationDegree = 0
fullCycleRound = 0

print ("\nturntable control script\n")
ser = serial.Serial ('COM1', 9600, timeout = 1) # configure seiral port
#ser.open()
print ("rotation angle is now", rotationDegree)

if ser.is_open == True:
    print ("serial port is openned")

    while rotationDegree < 360 :
        #print ("rotation angle is now", rotationDegree)
        ser.write(b'Step CW\r\n')  # write serial command to turntable
        time.sleep(11)             # wait at least 11 sec to execute next command
        rotationDegree += 10

        s = ser.read(10)
        print (s)
        print ("rotation angle is now", rotationDegree)
        
        #countDown = 11
        #while (countDown >= 11):
            #if countDown != 0 :
                #print (countDown)
                #countDown -= 1
            #else :
                #print ("Next!")
                #break
        
    if rotationDegree >= 360 :
        fullCycleRound += 1
        print ("one full cycle rotation completed")
        print ("rotation cycle is now",fullCycleRound)
        #time.sleep(15)
        #s = ser.read(10)
        #print (s)
    #else :
        #print ("something wrong here")    
else :
    ser.close()
    if ser.is_close == True:
        print ("serial port is closed\n script stop")
        #time.sleep(15)
        #s = ser.read(10)
        #print s
exit()
