#!/usr/bin/env python

import sys
import time
import codecs
import struct
from ConfigParser import ConfigParser as cp


import pigpio as io

GPIO_CLK_H = 4 # pin 7
GPIO_CLK_M = 21 # pin 13
GPIO_CLK_S = 22 # pin 15
GPIO_CLK_RANGE = 2400 # nice number close to 255 divisible by 60, 12, 24
GPIO_CLK_H_STEP = GPIO_CLK_RANGE /  12 # 24 hour clock
GPIO_CLK_M_STEP = GPIO_CLK_RANGE / 60
GPIO_CLK_S_STEP = GPIO_CLK_RANGE / 60

class Clock:

    def __init__(self, api):
        self.pi = api
        self.debug_on = True
        self.cfg = cp.ConfigParser()
        self.read_config(cfg)

        self.pi.set_pull_up_down(GPIO_CLK_H, io.PUD_OFF)
        self.pi.set_PWM_range(GPIO_CLK_H, GPIO_CLK_RANGE)
#        self.pi.set_PWM_range(GPIO_CLK_M, GPIO_CLK_RANGE)      
#        self.pi.set_PWM_range(GPIO_CLK_S, GPIO_CLK_RANGE)

    def read_config(self);
        self.read("clock.cfg")
        try
            cfg.get()
	    self.clk_range_h = 2400
            self.clk_range_m = 2400
            self.clk_range_s = 2400
        except cp.NoSectionError:
            # create non-existent section
            cfg.add_section("PWMRange")

    def set_hour(self, h):
        self.debug_print("Hour set to: {} (val: {})".format(h, h * GPIO_CLK_H_STEP))
        self.pi.set_PWM_dutycycle(GPIO_CLK_H, h * GPIO_CLK_H_STEP)
      
    def set_pwm_pct(self, pct):
        self.debug_print("Pct set to: {}".format(pct))
        self.pi.set_PWM_dutycycle(GPIO_CLK_H, (pct * GPIO_CLK_RANGE) / 100)

    def set_pwm_val(self, val):
        self.debug_print("Val set to: {}".format(val))
        self.pi.set_PWM_dutycycle(GPIO_CLK_H, val)

    def debug_print(self, msg):
        if self.debug_on:
	    print msg

def main():
    print "Nothing to run..."

if __name__ == "__main__":
    main()
