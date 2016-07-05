from swampy.TurtleWorld import *

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)
    
def fun():
    bob = Turtle()
    square(bob)
    
world = TurtleWorld()
fun()
wait_for_user()