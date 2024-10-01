def sub(a, b):
    if type(a) == type(b):
        if hasattr(a, '__sub__'):
            return a - b
        else:
            res = []
            for elem in a:
                if elem not in b:
                    res.append(elem)
            if type(a) == list:
                return res
            return tuple(res)


a, b = eval(input())
print(sub(a, b))

