from math import *

funcs = {}
strs = 1
while (line := input())[:5] != "quit ":
    if line[0] == ':':
        func_desc = line[1:].split()
        params = func_desc[1:-1]
        funcs[func_desc[0]] = (params, func_desc[-1])
        strs += 1
    else:
        strs += 1
        call = line.split()
        func_name = call[0]
        args = call[1:]
        print(eval(funcs[func_name][1], globals(), {param: eval(arg) for param, arg in zip(funcs[func_name][0], args)}))
print(line[6:-1].format(len(funcs) + 1, strs))
