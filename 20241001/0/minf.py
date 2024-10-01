def MINF(*funcs):
    def g(x):
        return min([f(x) for f in funcs])
    return g
