import math

epsilon = 0.0000001
def my_sqrt(x):
    x = float(x)
    a = x
    while True:
        y = (x + a / x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return y

if __name__ == '__main__':
    for i in range(1, 10):
        i = float(i)
        print "%.1f  %.11f  %.11f  %.11e" % (i, my_sqrt(i), math.sqrt(i), abs(my_sqrt(i) - math.sqrt(i)))