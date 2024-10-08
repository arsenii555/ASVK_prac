from fractions import Fraction
from decimal import Decimal


def esum(N, one):
    res = one
    fact = one
    for i in range(1, N):
        res += one / fact
        fact *= (i + 1) 
    return res


print(esum(100, Decimal(1))) 
