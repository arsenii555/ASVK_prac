def walk2d():
    new = yield (coord := (0, 0))
    while new:
        coord = coord[0] + new[0], coord[1] + new[1]
        new = yield coord


g = walk2d()
next(g)
for dx, dy in zip(range(10), range(-20, -10)):
    print(g.send((dx, dy)))

