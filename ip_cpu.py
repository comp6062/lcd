########################################################################
# Filename    : ip_cpu.py
# Description : Display CPU temp & Ip Address on 1602 LCD
# Author      : Kyle Downs & Alexander Travis
# modification: 2022/11/21
#################################

#! /usr/bin/env python

import drivers
from time import sleep
from datetime import datetime
from subprocess import check_output
display = drivers.Lcd()

def CPU():     # get CPU temperature from file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '  CPU: {:.2f}'.format( float(cpu)/1000 ) + ' C'


IP =' IP: ' + check_output (["hostname", "-I"]).split()[0]
try:

    print("Writing to display")
    while True:
        display.lcd_display_string(str(CPU()), 1)
        display.lcd_display_string(str(IP), 2)
        # Uncomment the following line to loop with 1 sec delay
        sleep(1)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

#text_string = <hide>("Alex, I love you more than you will ever know. You make me so proud that you are my son. 
#You are so smart you sometimes you make me feel like you're teaching me. This is the code that your ideas from your brain 
#inspired me to write. Completed: 11/21/2022. BIG DADDY HUG!!!)</hide>


