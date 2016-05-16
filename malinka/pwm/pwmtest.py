#!/usr/bin/env python

import sys
import time
import codecs
import struct

import pigpio
from pigpioclock import Clock

pi1 = pigpio.pi()       # pi1 accesses the local Pi's gpios

clk = Clock(pi1)

# clk.set_hour(1)

clk.debug_on = True

delay = 1
for k in range(10):
	for i in range(12):
	   clk.set_hour(i)
	   time.sleep(delay)
	for j in reversed(range(12)):
	   clk.set_hour(j)
	   time.sleep(delay)

#	pi1.write(4, 0) # set gpio 4 low
#	print pi1.read(4)
#	pi1.write(4, 1) # set gpio 4 to high
#	print pi1.read(4)     # get level of gpio 4



