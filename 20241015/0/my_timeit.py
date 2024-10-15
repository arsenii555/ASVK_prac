import timeit


s = input()
t = timeit.Timer(s).autorange()
print(t)
