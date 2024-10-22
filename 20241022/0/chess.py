from itertools import product


l = [f'{r}{c}' for r, c in product("ABCDEFGH", range(1, 9))]
print(l)