def closure(a, b):
    def func(x):
        return a * x + b
    return func

