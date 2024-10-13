from fractions import Fraction


def is_root(s, w, dgr_a, *params):
    s = Fraction(str(s))
    w = Fraction(str(w))
    coeffs_a = list(map(lambda x: Fraction(str(x)), params[0: dgr_a + 1]))
    dgr_b = params[dgr_a + 1]
    coeffs_b = list(map(lambda x: Fraction(str(x)), params[dgr_a + 2:]))
    nominator = sum(map(lambda x: x[1] * s ** (dgr_a - x[0]), enumerate(coeffs_a, 0)))
    denominator = sum(map(lambda x: x[1] * s ** (dgr_b - x[0]), enumerate(coeffs_b, 0)))
    if denominator and Fraction(nominator, denominator) == w:
        return True
    return False


inp = eval(input())
print(is_root(*inp))
