from swampy.TurtleWorld import *

def polyon(t, length, n):
    degree = 360 / n
    for i in range(n):
        fd(t, length)
        lt(t, degree)
    
def fun():
    bob = Turtle()
    polyon(bob, 50, 5)
    
world = TurtleWorld()
fun()
wait_for_user()