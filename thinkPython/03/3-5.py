def print_line(val1, val2):
    print val1,
    print val2, val2, val2, val2, 
    print val1,
    print val2, val2, val2, val2, 
    print val1
    
print_line('+', '-')
for i in range(4):
    print_line('|', ' ')
print_line('+', '-')
for i in range(4):
    print_line('|', ' ')
    print_line('+', '-')
