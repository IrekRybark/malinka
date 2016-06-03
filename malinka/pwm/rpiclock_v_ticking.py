from pygame_sdl2 import mixer 

from clockmvc import ClockView
from config import Config


class RPiClockViewTicking(ClockView):
    """
    The class is responsible for producing sound of clock ticking.
    """
    
    def __init__(self):
        super(RPiClockViewTicking, self).__init__()
        self.view_name = 'RPiTicking'
        
        mixer.init()
        
        self.cfg = Config('clock.cfg')
        self.sound_ticking = mixer.Sound(self.cfg.chimes_ticking_sound)
        
        self.last_played_second = None
        
        if mixer.get_num_channels() < 1:
            raise Exception('mixer does not have any channels')
        self.channel = mixer.Channel(0)
        
    def show(self):
        """ """ 
        second_now = self.time.second
        if self.last_played_second == None:
            self.last_played_second = second_now  # do not make sound when starting up
            
        if self.last_played_second != second_now:
            self.last_played_second = second_now
            
            self.channel.play(sound)


