import datetime
import time

from observable import Observable


class ClockModel():
    """
    The class is responsible for handling time.
    Specifically, it can retrieve time form the environment (OS) or dedicated hardware.
    """
    def __init__(self, time):
        self.time = Observable(time)

    def update_time(self, time):
        self.time.set(time)

    def get_hour(self):
        return self.time.hour

    def get_minute(self):
        return self.time.minute

    def get_second(self):
        return self.time.second


class ClockView():
    """
    The class is responsible for presenting time.
    The time can be shown in traditional way using clock face or some other method like binary numbers or voltmeters.
    """

    def set_time(self, time):
        self.time = time
        self.show()

    def show(self):
        print "Set time: ", self.time.hour, ":", self.time.minute, ":", self.time.second


class ClockController():
    """
    The class is responsible for updating attached view(s) based on changing values from model.
    """
    def __init__(self):
        self.model = ClockModel(datetime.datetime.now())
        self.view = ClockView()
        self.model.time.add_callback(self._time_changed)

    def _time_changed(self, time):
        self.view.set_time(time)

    def update_time(self, time):
        self.model.update_time(time)


def main():
    controller = ClockController()
    delay = 3
    controller.update_time(datetime.datetime.now())
    time.sleep(delay)
    controller.update_time(datetime.datetime.now())
    time.sleep(delay)
    controller.update_time(datetime.datetime.now())




if __name__ == "__main__":
    main()