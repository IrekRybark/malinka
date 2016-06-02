from pygame_sdl2 import mixer 

from clockmvc import ClockView
from config import Config


class RPiClockViewChimes(ClockView):
    """
    The class is responsible for presenting time (hours, half-hours)
    as sounds (chimes).
    """
    
    def __init__(self):
        super(RPiClockViewChimes, self).__init__()
        self.view_name = 'RPiChimes'
        
        mixer.init()
        
        self.cfg = Config('clock.cfg')
        self.sound_hour = mixer.Sound(self.cfg.chimes_hour_sound)
        self.sound_halfhour = mixer.Sound(self.cfg.chimes_halfhour_sound)
        
        self.last_played_minute = None
        
        if mixer.get_num_channels() < 1:
            raise Exception('mixer does not have any channels')
        self.channel = mixer.Channel(0)
        
    def show(self):
        """ """ 
        # ToDo: fix the test intervals 
        minute_now = self.time.minute
        if self.last_played_minute == None:
            self.last_played_minute = minute_now  # do not make sound when starting up
        if self.last_played_minute != minute_now:
            self.last_played_minute = minute_now
            
            count = (minute_now % 10)  # 0...9
            if count == 0:
                count = 9  # 10 times
            else:
                count -= 1 # count + 1 times
                
            if minute_now % 2 == 0:
                sound = self.sound_hour
            else:
                sound = self.sound_halfhour
            
            self.play_hour(sound, count) 

    def play_hour(self, sound, hour=0):
        
        self.channel.play(sound, hour)

