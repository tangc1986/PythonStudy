from swampy.TurtleWorld import *
import math

def circle(t, r):
    n = 10
    length = math.pi * r * 2 / n
    polyon(t, length, n)
    

def polyon(t, length, n):
    degree = 360 / n
    for i in range(n):
        fd(t, length)
        lt(t, degree)
    
def fun():
    bob = Turtle()
    bob.delay = 0.01
    circle(bob, 50)
    
world = TurtleWorld()
fun()
wait_for_user()