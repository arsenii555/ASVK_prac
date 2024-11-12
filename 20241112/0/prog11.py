from math import *

def divisor(a, b):
    eps = 1e-6
    if abs(b) < eps:
        raise ValueError
    else:
        return a / b

def proxy(fun, *args):
    try:
        return fun(*args)
    except ZeroDivisionError:
        return inf
    else:
        return "Divide yourself!"

