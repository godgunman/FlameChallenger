#!/usr/bin/python

# http://pyserial.sourceforge.net/

import serial

port = '/dev/tty.usbserial-DAWR13BI'
ser = serial.Serial(port, 9600, timeout=1)

# start
ser.write(bytearray([255,0,254]))

# stop
ser.write(bytearray([255,0,0]))
