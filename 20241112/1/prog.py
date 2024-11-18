from collections import UserString


class DivStr(UserString):
    def __init__(self, s=None):
        if s is None:
            self.data = ''
        else:
            super().__init__(s)

    def __floordiv__(self, other):
        res = []
        for i in range(0, len(self), step := len(self) // other):
            if i + step <= len(self):
                res.append(self.__class__(self.data[i:i + step]))
        return iter(res)

    def __mod__(self, other):
        return self.__class__(self.data[-(len(self) % other):])


import sys

exec(sys.stdin.read())
