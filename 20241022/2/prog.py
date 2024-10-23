from itertools import *


def slide(seq, n):
    it = iter(seq)
    result = tuple(islice(it, n))
    yield from result
    for elem in it:
        result = result[1:] + (elem,)
        yield from result
    for _ in result:
        result = result[1:]
        yield from result


import sys
exec(sys.stdin.read())
