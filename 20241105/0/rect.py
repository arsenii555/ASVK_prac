class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.__class__.rectcnt}", self)

    def __str__(self):
        return f'({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1}), {self.__class__.rectcnt}'

    def __lt__(self, other):
        if abs((self.x1 - self.x2) * (self.y1 - self.y2)) < abs(
                (other.x1 - other.x2) * (other.y1 - other.y2)):
            return True
        return False

    def __eq__(self, other):
        if abs((self.x1 - self.x2) * (self.y1 - self.y2)) == abs(
                (other.x1 - other.x2) * (other.y1 - other.y2)):
            return True
        return False

    def __mul__(self, other):
        return self.__class__(
            self.x1 * other,
            self.y1 * other,
            self.x2 * other,
            self.y2 * other)

    __rmul__ = __mul__

    def __getitem__(self, index):
        return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2),
                (self.x2, self.y1))[index]

    def __abs__(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

    def __bool__(self):
        return self.__abs__() != 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.__class__.rectcnt)


rect1 = Rectangle(5, 5, 5, 5)
rect2 = Rectangle(0, 0, 2, 2)
