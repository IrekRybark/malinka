from clockmvc import ClockController
from config import Config
from rpiclock_v_meters import RPiClockViewMeters
from rpiclock_v_chimes import RPiClockViewChimes


class RPiClockController(ClockController):

    def __init__(self):
        super(RPiClockController, self).__init__()
        self.add_view(RPiClockViewMeters())
        self.add_view(RPiClockViewChimes())

if __name__ == "__main__":
    pass
