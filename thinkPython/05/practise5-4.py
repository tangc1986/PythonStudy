from swampy.TurtleWorld import *

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length * n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2 * angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length * n)
    
world = TurtleWorld()
world.delay = 1
bob = Turtle()
draw(bob, 100, 2)
wait_for_user()