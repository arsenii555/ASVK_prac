from itertools import filterfalse


def ffn(n, seq):
    return filterfalse(lambda x: x % n != 0, seq)

print(list(ffn(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))