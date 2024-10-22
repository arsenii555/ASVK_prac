def row_summ():
    s = 0
    i = 1
    while True:
        s += 1 / (i ** 2)
        i += 1
        yield s


for i in zip(row_summ(), range(200)):
    print(i)