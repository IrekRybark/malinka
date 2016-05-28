
import ConfigParser as cp


class Config:

    def __init__(self, filename):
        self.filename = filename

        self.conf = cp.ConfigParser()
        self.conf.read(filename)

        self.pwm_range_h = self.conf.get("PWMRange", "hours")
        self.pwm_range_m = self.conf.get("PWMRange", "minutes")
        self.pwm_range_s = self.conf.get("PWMRange", "seconds")
        
        self.gpio_pin_h = self.conf.get("GPIOPin", "hours")
        self.gpio_pin_m = self.conf.get("GPIOPin", "minutes")
        self.gpio_pin_s = self.conf.get("GPIOPin", "seconds")

    def save_pwm_ranges(self):
        """ Save PWM range data to the configuration
        :return: nothing
        """
        self.conf["PWMRange"]["hours"] = self.pwm_range_h
        self.conf["PWMRange"]["minutes"] = self.pwm_range_m
        self.conf["PWMRange"]["seconds"] = self.pwm_range_s

        self.conf.write(self.filename)



def main():
    pass
    
if __name__ == "__main__":
    main()
    
