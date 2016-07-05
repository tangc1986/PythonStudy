from swampy.TurtleWorld import *

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)
    
def fun():
    bob = Turtle()
    square(bob, 50)
    
world = TurtleWorld()
fun()
wait_for_user()