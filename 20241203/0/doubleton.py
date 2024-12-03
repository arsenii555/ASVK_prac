class Doubleton(type):
    _instance1 = None
    _instance2 = None
    _count = 0

    def __call__(cls, *args, **kw):
        Doubleton._count += 1
        if Doubleton._count % 2 == 0:
            if cls._instance1 is None:
                 cls._instance1 = super().__call__(*args, **kw)
            return cls._instance1
        else:
            if cls._instance2 is None:
                cls._instance2 = super().__call__(*args, **kw)
            return cls._instance2


class S(metaclass=Doubleton):
    A = 3
s, t, r = S(), S(), S()
s.newfield = 100500
t.newfield = 100501
r.newfield = 100502
print(f"{s.newfield=}, {t.newfield=}")
print(f"{s is t=}")
print(*[S() for _ in range(10)], sep="\n")