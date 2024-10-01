from math import *


def Calc(s, t, u):
    def f(x):
        x, y = eval(s), eval(t)
        return eval(u)
    return f


s, t, u = eval(input())
x = eval(input())
F = Calc(s, t, u)
print(F(x))

