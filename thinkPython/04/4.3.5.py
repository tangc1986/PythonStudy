from swampy.TurtleWorld import *
import math

def arc(t, r, angle):
    n = 30
    length = (angle * math.pi) / 180 * r / n
    polyon(t, length, n, angle)

def polyon(t, length, n, angle):
    degree = angle / n
    for i in range(n):
        fd(t, length)
        lt(t, degree)
    
def fun():
    bob = Turtle()
    bob.delay = 0.01
    arc(bob, 50, 270)
    
world = TurtleWorld()
fun()
wait_for_user()