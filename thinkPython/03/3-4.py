def do_twice(f, value):
    f(value)
    f(value)

def print_spam(value):
    print value

#do_twice(print_spam, 'spam')

def do_four(fun, value):
    for i in range(4):
        fun(value)
        
do_four(print_spam, 'spam')