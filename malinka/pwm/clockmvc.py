import datetime
import time

from observable import Observable

class ClockModel(object):
    """
    The class is responsible for handling time.
    Specifically, it can retrieve time form the environment (OS), which is default or overridden to read from some
    other source (like hardware clock)
    """
    def __init__(self):
        self.time = Observable(datetime.time)

    def update_time(self):
        self.time.set(datetime.datetime.now())

    def get_hour(self):
        return self.time.hour

    def get_minute(self):
        return self.time.minute

    def get_second(self):
        return self.time.second


class ClockView(object):
    """
    The base class responsible for presenting time.
    The time can be shown in traditional way using clock face or some other method like binary numbers or voltmeters.
    Override show() to implement other methods of rendering time.
    """

    def set_time(self, time):
        self.time = time
        self.show()

    def show(self):
        print "Set time: ", self.time.hour, ":", self.time.minute, ":", self.time.second


class ClockController(object):
    """
    The class is responsible for updating attached view(s) based on changing values from model.
    """
    def __init__(self):
        self.model = self.make_model()
        self.views = []
        self.add_view(self.make_view())
        self.model.time.add_callback(self._time_changed)

    def make_model(self):
        return ClockModel()

    def make_view(self):
        return ClockView()

    def add_view(self, view):
        self.views.append(view)

    def del_view(self, view):
        for v in self.views:
            if v is view:
                self.views.remove(v)

    def _time_changed(self, time):
        for v in self.views:
            v.set_time(time)

    def update_time(self):
        self.model.update_time()


def main():
    pass

if __name__ == "__main__":
    main()
