import random

def has_duplicates(lst):
    for i in range(len(lst)-1):
        if lst[i] in lst[i+1:]:
            return True
    return False

def gen_birth():
    month = random.randint(1,12)
    if month == 2:
        day = random.randint(1,29)
    elif month in [1,3,5,7,8,10,12]:
        day = random.randint(1,31)
    else:
        day = random.randint(1,30)
    return month*100+day

count = 0
for i in range(100000):
    all_birth = []
    for i in range(23):
        all_birth.append(gen_birth())
    if has_duplicates(all_birth):
        count += 1

print float(count)/100000
        



