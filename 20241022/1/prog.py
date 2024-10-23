def fib(m, n):
    res = [1, 1]
    for i in range(2, m + n):
        res.append(res[i - 2] + res[i - 1])
    return iter(res[m:m + n])


import sys
exec(sys.stdin.read())
