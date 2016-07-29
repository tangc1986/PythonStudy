for i in range(1, 1000000):
    num = i
    num1 = num % 10
    num2 = num/10 % 10
    num3 = num/100 % 10
    num4 = num/1000 % 10
    num5 = num/10000 % 10
    num6 = num/100000 % 10
    if not (num1 == num4 and num2 == num3):
        continue
    num = num + 1
    num1 = num % 10
    num2 = num/10 % 10
    num3 = num/100 % 10
    num4 = num/1000 % 10
    num5 = num/10000 % 10
    num6 = num/100000 % 10
    if not (num1 == num5 and num2 == num4):
        continue
    num = num + 1
    num1 = num % 10
    num2 = num/10 % 10
    num3 = num/100 % 10
    num4 = num/1000 % 10
    num5 = num/10000 % 10
    num6 = num/100000 % 10
    if not (num2 == num5 and num3 == num4):
        continue
    num = num + 1
    num1 = num % 10
    num2 = num/10 % 10
    num3 = num/100 % 10
    num4 = num/1000 % 10
    num5 = num/10000 % 10
    num6 = num/100000 % 10
    if not (num1 == num6 and num2 == num5 and num3 == num4):
        continue
    print i
    