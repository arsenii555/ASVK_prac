class Num:
    def __get__(self, obj, cls):
        if hasattr(obj, '_val'):
            return obj._val
        return 0

    def __set__(self, obj, value):
        if hasattr(value, 'real'):
            obj._val = value
        elif hasattr(value, '__len__'):
            obj._val = len(value)

    def __delete__(self, obj):
        if hasattr(obj, '_val'):
            del obj._val


import sys
exec(sys.stdin.read())
