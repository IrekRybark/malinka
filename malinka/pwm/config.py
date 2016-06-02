
import ConfigParser as cp


class Config:

    def __init__(self, filename):
        self.filename = filename

        self.conf = cp.ConfigParser()
        self.conf.read(filename)

        self.clock_24h = self.conf.getboolean("Clock", "mode24h")

        self.chimes_hour_sound = self.conf.get("Chimes", "hour_sound")
        self.chimes_halfhour_sound = self.conf.get("Chimes", "halfhour_sound")
        
        self.pwm_range_h = self.conf.getint("PWMRange", "hours")
        self.pwm_range_m = self.conf.getint("PWMRange", "minutes")
        self.pwm_range_s = self.conf.getint("PWMRange", "seconds")
        
        self.gpio_pin_h = self.conf.getint("GPIOPin", "hours")
        self.gpio_pin_m = self.conf.getint("GPIOPin", "minutes")
        self.gpio_pin_s = self.conf.getint("GPIOPin", "seconds")
        


 
def main():
    pass
    
if __name__ == "__main__":
    main()
    
