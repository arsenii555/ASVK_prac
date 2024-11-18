class Undead(Exception):
    pass


class Zombie(Undead):
    pass


class Skeleton(Undead):
    pass


class Ghoul(Undead):
    pass


def necro(a):
    raise d[a % 3]()


d = {0: Skeleton, 1: Zombie, 2: Ghoul}
x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print('Skeleton')
    except Zombie:
        print('Zombie')
    except Undead:
        print("Generic Undead")
