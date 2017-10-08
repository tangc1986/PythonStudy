def myzip(*args):
    iters = list(map(iter, args))
    print(iters)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

print(list(myzip('abc', 'lmnop')))
