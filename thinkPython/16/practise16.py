class Time(object):
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

def print_time(time):
    print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)
    
def if_after(t1, t2):
    time1 = t1.second + (t1.minute + t1.hour*60)*60
    time2 = t2.second + (t2.minute + t2.hour*60)*60
    return time1 > time2

def increment(time, seconds):
    time.second += seconds
    
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
        
    if (time.second >= 60 or time.minute >=60):
        increment(time, 0)


time = Time()
time.hour = 0
time.minute = 0
time.second = 0

print_time(time)
increment(time, 18000)
print_time(time)
