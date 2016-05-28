import datetime
import time

import pigpio

from clockmvc import ClockController, ClockView
from config import Config


class TimePart():

    def __inint__(self, gpio_pin, pwm_range, increment):
        self.gpio_pin = gpio_pin
        self.pwm_range = pwm_range
        self.increment = increment
        self.step = pwm_range / increment
    
    def duty_cycle(self, part_value):
        return part_value * self.step 


class RPiClockViewMeters(ClockView):
    """
    The class is responsible for presenting time.
    The time can be shown in traditional way using clock face or some other method like binary numbers or voltmeters.
    """
    def __init__(self):
        super(RPiClockViewMeters, self).__init__()
        self.view_name = 'RPiPWM'
        
        self.cfg = Config('clock.cfg')
        time_parts = dict([
             ("h", TimePart(self.cfg.gpio_pin_h, self.cfg.pwm_range_h, 12)),
             ("m", TimePart(self.cfg.gpio_pin_m, self.cfg.pwm_range_m, 60)),
             ("s", TimePart(self.cfg.gpio_pin_s, self.cfg.pwm_range_s, 60)),
            ])
        
        self.pi = pigpio.pi()       # pi accesses the local Pi's gpios
        for p in time_parts:
            self.set_gpio_range(p.gpio_pin, p.pwm_range)


    def set_time(self, time):
        self.time = time
        self.show()

    def get_time_part(part):
        return {
            "h": self.time.hour,
            "m": self.time.minute,
            "s": self.time.second,
            }[part]
    
    def show(self):
        print self.view_name
        print "Hour meter:    ", self.time.hour
        print "Minute meter:  ", self.time.minute
        print "Second meters: ", self.time.second

        for p in time_parts:
            self.pi.set_PWM_dutycycle(p.gpio_pin, p.duty_cycle(get_time_part(p)))


class RPiClockController(ClockController):

    def make_view(self):
        # super(RPiClockController, self).ma
        return RPiClockViewMeters()

def main():
    controller = RPiClockController()
    delay = 3
    controller.update_time()
    time.sleep(delay)

    new_view = RPiClockViewMeters()
    controller.add_view(new_view)
    new_view.view_name = 'RPi2'
    controller.update_time()

    time.sleep(delay)

    controller.del_view(new_view)
    controller.update_time()


if __name__ == "__main__":
    main()
