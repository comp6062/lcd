

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
    return 'CPU TEMP:{:.2f}'.format( float(cpu)/1000 ) + ' C'


IP = check_output(["hostname", "-I"]).split()[0]
try:
    print(
"Writing to display")
    while True:
        display.lcd_display_string(str(CPU()), 1)
        display.lcd_display_string(str(IP), 2)
        # Uncomment the following line to loop with 1 sec delay
        sleep(.75)
except KeyboardInterrupt:
    # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()

