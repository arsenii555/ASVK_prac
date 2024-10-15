from collections import Counter
import timeit
s = input()

def f1():
    return len({w: 0 for w in s.split()})

def f2():
    return len(Counter(s.split()))


print(timeit.Timer(f1).autorange())
print(timeit.Timer(f2).autorange())
