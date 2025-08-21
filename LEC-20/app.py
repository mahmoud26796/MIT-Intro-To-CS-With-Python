from dateutil import parser
class Workout(object):
    cal_per_hour = 200

    def __init__(self, start, end, calories=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end) 
        self.calories = calories
        self.icon = '😅'
        self.kind = 'Workout'
    
    def get_calories(self):
        if(self.calories == None):
            return Workout.cal_per_hour * (self.end - self.start).total_seconds() / 3600
        else: 
            return self.calories
    def get_duration(self):
        return self.end - self.start
    def __str__(self):
        width = 16
        retstr = f" | {'-' * width} | \n"
        retstr += f" | {' ' * width} | \n"
        iconLen = len(self.icon)
        retstr += f" | {self.icon} {' '*(width - iconLen -2 )} | \n"
        retstr += f" | {self.kind} {' '*(width - len(self.kind)  - 1)} | \n"
        retstr += f" | {' ' * width} | \n"
        retstr += f" | {' ' * width} | \n"
        duration_str = str(self.get_duration())
        retstr += f" | {duration_str} {' '*(width - len(duration_str)  - 1)} | \n"
        cal_str = str(self.get_calories())
        retstr += f" | {cal_str} Cal{' '*(width - len(cal_str) - 3 )}|\n"
        retstr += f" | {' ' * width} | \n"
        retstr += f" | {' ' * width} | \n"
        return retstr

w1 = Workout('8/17/2025 1:00 AM', '8/17/2025 3:00 AM', 400)
w2 = Workout('8/17/2025 1:00 AM', '8/17/2025 3:00 AM')

# print(w1.get_calories())
# print(w2.get_calories())

print(w1)

# Running Workout class 
class Running_Workout(Workout):
    def __init__(self, start, end, elev = 0, calories=None):
        super().__init__(start, end, calories)
        self.elev = elev
        self.icon = '🏃'
        self.kind = 'Running'
    def set_elev(self, e):
        self.elev = e
    def get_elev(self):
        return self.elev

rw1 = Running_Workout('8/17/2025 1:00 AM', '8/17/2025 1:30 AM', 3)
print(rw1)