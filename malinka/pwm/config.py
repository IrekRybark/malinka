
import ConfigParser as cp


class Config:

    def __init__(self, filename):
        self.filename = filename

        conf = cp.ConfigParser()
        conf.read(filename)

        self.pwm_range_h = conf["PWMRange"]["hours"]
        self.pwm_range_m = conf["PWMRange"]["minutes"]
        self.pwm_range_s = conf["PWMRange"]["seconds"]




def main():
    pass
    
if __name__ == "__main__":
    main()
    
