class Sole(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError(f"Only one parent")
        return super().__new__(metacls, name, parents, namespace)


class C(metaclass=Sole):
    pass

class D(metaclass=Sole):
    pass


class E(C, D, metaclass=Sole):
    pass