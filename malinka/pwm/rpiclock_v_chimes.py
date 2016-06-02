from pygame_sdl2 import mixer 

from clockmvc import ClockView
from config import Config


class MinuteChime():

    def __init__(self, sound, at_minute, repetitions):
        self.last_played_hour = None
        self.sound = sound
        self.at_minute = at_minute
        self.repetitions = repetitions

    def get_repetitions(self):
        if
       
class RPiClockViewChimes(ClockView):
    """
    The class is responsible for presenting time (hours, half-hours, quarters etc.)
    as sounds (chimes).
    """
    
    def __init__(self):
        super(RPiClockViewChimes, self).__init__()
        self.view_name = 'RPiChimes'
        
        mixer.init()
        
        self.cfg = Config('clock.cfg')
        self.sound_hour = mixer.Sound(self.cfg.chimes_hour_sound)
        self.sound_halfhour = mixer.Sound(self.cfg.chimes_halfhour_sound)

        self.schedule = [
            MinuteChime(self.sound_hour, 0, lambda(x, x%12 if x%12 != 0 else 12)),
            MinuteChime(self.sound_halfhour, 15, "1"),
            MinuteChime(self.sound_halfhour, 30, "2"),
            MinuteChime(self.sound_halfhour, 45, "3"),
            ]
        
        self.last_played_hour = None
        self.last_played_halfhour = None
        self.last_played_minute = None
        
        if mixer.get_num_channels() < 1:
            raise Exception('mixer does not have any channels')

        self.channel = mixer.Channel(0)
        
    def show(self):
        """ """ 
        
        def show_time(chime, minute_now, hour_now):
            if (chime.last_played_hour == None) or (chime.last_played_hour != hour_now):
                if chime.at_minute == minute_now:
                    chime.last_played_hour = hour_now
                    if chime.repetitions == "hour":
                        repetitions = hour_now % 12 if hour_now % 12 != 0 else 12
                    else:
                        repetitions = int(chime.repetitions)
                    self.play_sound(chime.sound, repetitions)
                
        def play_sound(sound, repetitions):
            print "Playing", repetitions, "times", sound, "sound"
            self.channel.play(sound, repetitions-1)
            
        minute_now = self.time.minute
        hour_now = self.time.hour
        
        for c in self.schedule:
             show_time(c, minute_now, hour_now)
            


