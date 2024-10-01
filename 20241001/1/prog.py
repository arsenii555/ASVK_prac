def Pareto(*args):
    res = []
    for i in range(len(args)):
        for j in range(len(args)):
            x, y = args[i]
            a, b = args[j]
            if i != j and x <= a and y <= b and (x < a or y < b):
                break
        else:
            res.append(args[i])
    return tuple(res)


data = eval(input())
print(Pareto(*data))
