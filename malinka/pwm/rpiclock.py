import datetime
import time

from clockmvc import ClockController, ClockView


class RPiClockViewMeters(ClockView):
    """
    The class is responsible for presenting time.
    The time can be shown in traditional way using clock face or some other method like binary numbers or voltmeters.
    """
    def __init__(self):
        super(RPiClockViewMeters, self).__init__()
        self.view_name = 'RPi'

        self.gpio_pin_h = 4
        self.gpio_pin_m = 21
        self.gpio_pin_s = 22

    def set_time(self, time):
        self.time = time
        self.show()

    def show(self):
        print self.view_name
        print "Hour meter:    ", self.time.hour
        print "Minute meter:  ", self.time.minute
        print "Second meters: ", self.time.second
#        self.pi.set_PWM_range(GPIO_CLK_H, GPIO_CLK_RANGE)
#        self.pi.set_PWM_range(GPIO_CLK_M, GPIO_CLK_RANGE)
#        self.pi.set_PWM_range(GPIO_CLK_S, GPIO_CLK_RANGE)


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