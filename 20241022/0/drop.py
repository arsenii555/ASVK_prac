from itertools import islice, dropwhile


def row_summ():
    s = 0
    i = 1
    while True:
        s += 1 / (i ** 2)
        i += 1
        yield s


print(*islice(dropwhile(lambda x: x <= 1.6, s := row_summ()), 0, 10), sep='\n')
