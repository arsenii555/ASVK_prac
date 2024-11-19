import sys
from pympler.asizeof import asizeof
from string import ascii_letters



class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


class Slotter:
    __slots__ = tuple(ascii_letters)

    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)


s = Slotter()
t = Trad()
print(dir(s))
print(s.T)
print(sys.getsizeof(Slotter))
print(sys.getsizeof(Trad))
print(sys.getsizeof(s))
print(sys.getsizeof(t))
print(asizeof(s))
print(asizeof(t))
t_list = [Trad() for _ in range(1000)]
s_list = [Slotter() for _ in range(1000)]
print(asizeof(t_list))
print(asizeof(s_list))