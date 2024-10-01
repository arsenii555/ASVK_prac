def rbin(n, lst, bit):
    if n - 1 == 0:
        print(lst + [bit])
        return
    else:
        rbin(n - 1, lst + [bit], 0)
        rbin(n - 1, lst + [bit], 1)

rbin(3, [], 1)
