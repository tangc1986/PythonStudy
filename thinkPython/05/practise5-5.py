from swampy.TurtleWorld import *

def koch(t, x):
    if x < 3.0:
        fd(t, x)
        return
    koch(t, x/3.0)
    lt(t, 60)
    koch(t, x/3.0)
    rt(t, 120)
    koch(t, x/3.0)
    lt(t, 60)
    koch(t, x/3.0)


def snowflake(t, x):
    koch(t, x)
    rt(t, 120)
    koch(t, x)
    rt(t, 120)
    koch(t, x)
    
    
world = TurtleWorld()
world.delay = 0
bob = Turtle()
snowflake(bob, 500)
wait_for_user()    