from clockmvc import ClockController
from config import Config
from rpiclock_v_meters import RPiClockViewMeters

class RPiClockController(ClockController):

    def __init__(self):
        super(RPiClockController, self).__init__()
        self.add_view(RPiClockViewMeters())

if __name__ == "__main__":
    pass
