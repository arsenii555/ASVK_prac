class A:
    __v = 0
    def inc(self):
        self.__v += 1
        print(self.__v)


class B(A):
    __v = 100500



a = A()
b = B()
a.inc()
a.inc()
b.inc()
a.inc()
