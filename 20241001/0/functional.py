def S(f, g):
    def func(x):
        return f(x) + g(x)
    return func
