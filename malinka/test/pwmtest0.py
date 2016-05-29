#!/usr/bin/env python

import malinka.pwm.pigpio_sim

pi1 = malinka.pwm.pigpio_sim.pi()       # pi1 accesses the local Pi's gpios
pi1.set_pull_up_down(4, malinka.pwm.pigpio_sim.PUD_OFF)
pi1.write(4, 0) # set gpio low
print pi1.read(4)


