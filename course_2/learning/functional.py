from functools import reduce
def f(x, y, z): return x*y+z


print(f(2, 3, 4))

print((lambda x, y, z:  x)(1, 2, 3))

fns = {
    'f1': lambda x, y: x*y,
    'f2': lambda x, y: x+y
}

print(fns['f1'](1, 2))


# mapppping
l = list(range(1, 5))


def inc(x):
    return x + 10


new_l = list(map(inc, l))
new_l_lambda = list(map(lambda x: x + 10, l))
print(new_l, new_l_lambda)
print(tuple(map(lambda x: x + 10, l)))


combinations = list(map(pow, [1, 2, 3], [4, 5, 6]))
print(combinations)

combinations_with_shorter = list(
    map(lambda x, y, z: x+y+z, [1, 2, 3], [4, 5, 6], [1, 2]))
print(combinations_with_shorter)


# FILTER
to_filter = list(range(1, 20))
filtered = list(filter(lambda x: x % 2 == 0, to_filter))
print(filtered)


# reusable
def pari(l): return filter(lambda x: x % 2 == 0, l)


print(reduce(lambda accumulator, current: accumulator * current, range(1, 10, 2)))
