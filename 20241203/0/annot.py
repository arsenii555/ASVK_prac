import inspect


class C:
    a: int

    def __init__(self, val):
        if isinstance(val, inspect.get_annotations(self.__class__)['a']):
            self.__class__.a = val
        else:
            raise TypeError


print(C(1).a)