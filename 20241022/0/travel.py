def travel(n):
    yield from ["по кочкам"] * n
    return "и в яму бух"


def travelwrap(n):
    res = yield from travel(n)
    yield res


print(list(travelwrap(4)))