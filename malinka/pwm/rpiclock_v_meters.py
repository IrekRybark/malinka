# set to false if simulating the library
if False:
    import pigpio
else:
    import pigpio_sim
    

from clockmvc import ClockView
from config import Config


class TimePart():
    """ 
    Class stores control parameters for a given part of time (hour, minute, etc.)
    """

    def __init__(self, gpio_pin, pwm_range, increment):
        self.gpio_pin = gpio_pin
        self.pwm_range = pwm_range
        self.increment = increment
        self.step = self.pwm_range / self.increment
    
    def duty_cycle(self, part_value):
        return part_value * self.step 


class RPiClockViewMeters(ClockView):
    """
    The class is responsible for presenting time using miliamp meterr 
    by means of changing duty cycle of PWM signals in RaspberryPi.
    """
    
    def __init__(self):
        super(RPiClockViewMeters, self).__init__()
        self.view_name = 'RPiPWM'
        
        self.cfg = Config('clock.cfg')
        self.mode24h = self.cfg.clock_24h
        self.time_parts = dict([
             ("h", TimePart(self.cfg.gpio_pin_h, self.cfg.pwm_range_h, 24 if self.mode24h else 12)),
             ("m", TimePart(self.cfg.gpio_pin_m, self.cfg.pwm_range_m, 60)),
             ("s", TimePart(self.cfg.gpio_pin_s, self.cfg.pwm_range_s, 60)),
            ])

        self.pi = pigpio_sim.pi() # pi accesses the local Pi's gpios
        # initialize PWM duty cycle ranges
        for p in self.time_parts:
            self.pi.set_gpio_range(self.time_parts[p].gpio_pin, self.time_parts[p].pwm_range)

#    def set_time(self, time):
#        """
#        :param time: time value 1-24
#        :return: nothing
#        """        
#        self.time = time
#        self.show()

    def hour_24_12(self, hour):
        """
        :param hour: time value 1-24
        :return: hour value 1-12 or 1-24 depending on 12/24 mode selection
        """
        if self.mode24h:
            return hour
        else:
            if hour > 12:
                return hour - 12
            else:
                return hour

    def get_time_part(self, part):
        """ Get part of time value (h, m, s).
        :param part: time part (h, m, s)
        :return: TimePart() object
        """        
        return {
            "h": self.hour_24_12(self.time.hour),
            "m": self.time.minute,
            "s": self.time.second,
            }[part]
    
    def show(self):
        """ Set PWM duty cycles for each time part on correspinding GPIO output
        :return: nothing
        """
        print self.time.hour, self.time.minute, self.time.second
        for p in self.time_parts:
            self.pi.set_PWM_dutycycle(self.time_parts[p].gpio_pin, self.time_parts[p].duty_cycle(self.get_time_part(p)))

