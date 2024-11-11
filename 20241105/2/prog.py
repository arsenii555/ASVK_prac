class Triangle:
    def __init__(self, a, b, c):
        self.a = tuple(a)
        self.b = tuple(b)
        self.c = tuple(c)

    def __abs__(self):
        def size(a, b):
            return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

        sizes = [size(self.a, self.b), size(self.b, self.c), size(self.c, self.a)]
        if 2 * max(sizes) < sum(sizes):
            return 0.5 * abs((self.b[0] - self.a[0]) * (self.c[1] - self.a[1]) - (self.c[0] - self.a[0]) * (self.b[1] - self.a[1]))
        return 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __bool__(self):
        return abs(self) > 0

    def __contains__(self, other):
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

        def point_in_triangle(pt, v1, v2, v3):
            b1 = sign(pt, v1, v2) <= 0.0
            b2 = sign(pt, v2, v3) <= 0.0
            b3 = sign(pt, v3, v1) <= 0.0
            return (b1 == b2) and (b2 == b3)

        if not self:
            return True
        if not other:
            return True
        return (point_in_triangle(other.a, self.a, self.b, self.c) and
                point_in_triangle(other.b, self.a, self.b, self.c) and
                point_in_triangle(other.c, self.a, self.b, self.c))

    def __and__(self, other):
        def ccw(A, B, C):
            return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

        def intersect(A, B, C, D):
            return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

        if not self or not other:
            return False

        edges1 = [(self.a, self.b), (self.b, self.c), (self.c, self.a)]
        edges2 = [(other.a, other.b), (other.b, other.c), (other.c, other.a)]

        for edge1 in edges1:
            for edge2 in edges2:
                if intersect(edge1[0], edge1[1], edge2[0], edge2[1]):
                    return True

        return self in other or other in self


import sys

exec(sys.stdin.read())
