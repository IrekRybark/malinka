

class Chime():
    def __init__(self, sound, at_minute, repetitions):
        self.sound = sound
        self.at_minute = at_minute
        self.repetitions = repetitions

    def get_reps(self, hour):
        return hour % 12 if hour % 12 != 0 else 12

### naive conversion

naive_chime_list = [
    Chime("hour_chime",     0, 'hour'),
    Chime("quarter_chime", 15, '1'),
    Chime("quarter_chime", 30, '2'),
    Chime("quarter_chime", 45, '3'),
]

def naive_chime(hour_now, minute_now):
    for l in naive_chime_list:
        if l.at_minute == minute_now:
            if l.repetitions == 'hour':
                reps = l.get_reps(hour_now)
            else:
                reps = int(l.repetitions)
            print "at minute", minute_now, "make sound", l.sound, reps, "times"

### using lambda function

lambda_chime_list = [
    Chime("hour_chime",     0, lambda h: h % 12 if h % 12 != 0 else 12),
    Chime("quarter_chime", 15, lambda h: 1),
    Chime("quarter_chime", 30, lambda h: 2),
    Chime("quarter_chime", 45, lambda h: 3),
]

def lambda_chime(hour_now, minute_now):
    for l in lambda_chime_list:
        if l.at_minute == minute_now:
            print "at minute", minute_now, "make sound", l.sound, l.repetitions(hour_now), "times"

### using eval

eval_chime_list = [
    Chime("hour_chime",     0, "h % 12 if h % 12 != 0 else 12"),
    Chime("quarter_chime", 15, "1"),
    Chime("quarter_chime", 30, "2"),
    Chime("quarter_chime", 45, "3"),
]

def eval_chime(hour_now, minute_now):
    for l in eval_chime_list:
        if l.at_minute == minute_now:
            h = hour_now
            print "at minute", minute_now, "make sound", l.sound, eval(l.repetitions), "times"

hour = 10
for min in range(0, 59):
    eval_chime(hour, min)

# at minute 0 make sound hour_chime 10 times
# at minute 15 make sound quarter_chime 1 times
# at minute 30 make sound quarter_chime 2 times
# at minute 45 make sound quarter_chime 3 times