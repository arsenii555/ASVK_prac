import pickle


class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

    def __str__(self):
        return f"{self.lst}, {self.dct}, {self.num}, {self.st}"


ser = SerCls([1, 2, 3], {1:'1', 2:'2'}, 123, "123")
print(ser)
ser_str = pickle.dumps(ser)
del ser
ser1 = pickle.loads(ser_str)
print(ser1)
