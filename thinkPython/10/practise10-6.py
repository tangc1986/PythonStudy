def is_sorted(lst):
    copy = lst[:]
    copy.sort()
    return lst == copy

print is_sorted([1, 5, 4])