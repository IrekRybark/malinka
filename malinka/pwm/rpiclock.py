import datetime
import time
from threading import Timer


from rpiclock_c import RPiClockController
from rpiclock_v_meters import RPiClockViewMeters
from config import Config


controller = RPiClockController()

def update():
    """ Trigger controller update and set the timer for the next update
    :param controller: controller object
    :return: nothing
    """
    controller.update_time()
    Timer(0.1, update, ()).start()  # can we use some interrupts for this

def main():
    
    # loop
    update()


if __name__ == "__main__":
    main()
