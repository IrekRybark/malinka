

class pi:
    """ Quick and dirty way to 'simulate' GPIO library
    """

    def set_gpio_range(self, user_gpio, range):
        print "set_gpio_range", user_gpio, range

    def set_PWM_dutycycle(self, user_gpio, dutycycle):
        print "set_PWM_dutycycle", user_gpio, dutycycle