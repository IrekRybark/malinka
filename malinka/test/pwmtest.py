#!/usr/bin/env python

import sys
import time
import codecs
import struct
import sched
from threading import Timer

# import pigpio
from malinka.pwm.pigpioclock import Clock

#pi1 = pigpio.pi()       # pi1 accesses the local Pi's gpios

clk = Clock(None)

s = sched.scheduler(time.time, time.sleep)

def print_time():
    print "From print_time", time.time()
    Timer(0.1, print_time, ()).start()


def print_some_times():
    print time.time()
    Timer(1, print_time, ()).start()
    print time.time()


print_some_times()

# clk.set_hour(1)

# clk.debug_on = True
#
# delay = 1
# for k in range(10):
#     for i in range(12):
#        clk.set_hour(i)
#        time.sleep(delay)
#     for j in reversed(range(12)):
#        clk.set_hour(j)
#        time.sleep(delay)
#
#    pi1.write(4, 0) # set gpio 4 low
#    print pi1.read(4)
#    pi1.write(4, 1) # set gpio 4 to high
#    print pi1.read(4)     # get level of gpio 4



