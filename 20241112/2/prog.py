class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def abs_tr(a, b, c):
    def size(a, b):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    sizes = [size(a, b), size(b, c), size(c, a)]
    if 2 * max(sizes) < sum(sizes):
        return 0.5 * abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))
    return 0


def triangleSquare(line):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(line)
    except Exception:
        raise InvalidInput('Invalid input')
    try:
        s = abs_tr((x1, y1), (x2, y2), (x3, y3))
    except TypeError:
        raise BadTriangle('Bad triangle')
    if s == 0:
        raise BadTriangle('Bad triangle')
    return s


while line := input():
    try:
        print(triangleSquare(line))
        break
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')

