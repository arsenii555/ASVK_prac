def objcount(cls):
    cls.counter = 0
    init = cls.__init__ if '__init__' in cls.__dict__ else None
    delete = cls.__del__ if '__del__' in cls.__dict__ else None

    def __init__(self, *args, **kwargs):
        cls.counter += 1
        if init:
            init(self, *args, **kwargs)

    def __del__(self):
        cls.counter -= 1
        if delete:
            delete(self)

    cls.__init__ = __init__
    cls.__del__ = __del__
    return cls


import sys
exec(sys.stdin.read())
