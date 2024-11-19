def fun(a,b):
    return a*2+b

def genf(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

newf = genf(fun)
print(newf(2,3))