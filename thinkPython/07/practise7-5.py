import math
def estimate_pi():
    k = 0
    f = 0
    while True:
        tmp = math.factorial(4 * k) * (1103 + 26390 * k) / (math.factorial(k) ** 4 * 396 ** (4 * k))
        f = f + tmp
        if tmp < 1e-15:
            return 1 / (2.0 * math.sqrt(2.0) / 9801.0 * f)
        k = k + 1
        
print estimate_pi()
print math.pi
        