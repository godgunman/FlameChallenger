#!/usr/bin/python

# http://pyserial.sourceforge.net/

import serial

port = '/dev/tty.usbserial-DAWR13BI'

class PumpSpark:

  ser = None
  def connect(self):
    try:
      self.ser = serial.Serial(port, 9600, timeout=1)
      print 'connected serial port.'
    except: 
      print 'connected fail.'
      pass

  def turnOff(self, *args):
    if len(args) == 0:
      for i in range(0, 8):
        self.ser.write(bytearray([255,i,0]))
    else:
      for i in args:
        self.ser.write(bytearray([255,i,0]))

  def turnOn(self, p, *args):
    if len(args) == 0:
      for i in range(0, 8):
        self.ser.write(bytearray([255,i,p]))
    else:
      for i in args:
        self.ser.write(bytearray([255,i,p]))

