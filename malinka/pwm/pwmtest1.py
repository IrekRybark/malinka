#!/usr/bin/env python

import sys
import time
import codecs
import struct

import pigpio

pi1 = pigpio.pi()       # pi1 accesses the local Pi's gpios
pi1.set_pull_up_down(4, pigpio.PUD_OFF)
pi1.write(4, 1) # set gpio to high
print pi1.read(4)     # get level of gpio
