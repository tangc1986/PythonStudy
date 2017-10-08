"""
Emulate most of the 3.0 print function for use in 2.x
call signature: print30(*args, sep=' ', end='\n', file=None)
"""

import sys

def print30(*args, sep=' ', end='\n', file=sys.stderr):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

