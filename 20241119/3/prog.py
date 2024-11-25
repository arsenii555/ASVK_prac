class Vowel:
    answer = 42
    __slots__ = tuple("aouiey")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__class__.__slots__:
                setattr(self, key, value)

    @property
    def full(self):
        for l in self.__class__.__slots__:
            if not getattr(self, l, None):
                return False
        return True

    @full.setter
    def full(self, value):
        pass

    def __str__(self):
        res = ""
        for l in sorted(self.__class__.__slots__):
            if getattr(self, l, None):
                res += f", {l}: {getattr(self, l, None)}"
        return res[2:]


import sys

exec(sys.stdin.read())


