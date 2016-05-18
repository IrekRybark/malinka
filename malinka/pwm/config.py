
import ConfigParser as cp


class Config:

    def __init__(self, filename):
        self.filename = filename

        self.conf = cp.ConfigParser()
        self.conf.read(filename)
        self.get()

    def get(self):
        self.pwm_range_h = self.conf["PWMRange"]["hours"]
        self.pwm_range_m = self.conf["PWMRange"]["minutes"]
        self.pwm_range_s = self.conf["PWMRange"]["seconds"]

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
    
