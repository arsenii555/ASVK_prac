from itertools import product


print(*sorted(filter(lambda x: x.count('TOR') == 2, [''.join(i) for i in product("TOR", repeat=int(input()))])), sep=', ')
