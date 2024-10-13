from math import *


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


def show(screen):
    print('\n'.join(''.join(row) for row in screen))


def graf(W, H, A, B, func):
    screen = [[' '] * W for _ in range(H)]
    X = list(range(W))
    X_scaled = [scale(0, W - 1, A, B, x) for x in X]
    Y = list(map(lambda x: eval(func), X_scaled))
    Y_scaled = []
    for y in Y:
        r = scale(min(Y), max(Y), 0, H - 1, y)
        if r - int(r) >= 0.5:
            Y_scaled.append(ceil(r))
        else:
            Y_scaled.append(floor(r))
    for x, y in zip(X, Y_scaled):
        screen[H - y - 1][x] = '*'
    for c in range(W):
        col = [screen[i][c] for i in range(H)]
        if col.count('*') > 1:
            indexes = [i for i, x in enumerate(col) if x == '*']
            for j in range(indexes[0], indexes[-1]):
                screen[j][c] = "*"
    for c in range(W - 1):
        curr = [screen[i][c] for i in range(H)]
        next = [screen[i][c + 1] for i in range(H)]
        next_last = ''.join(next).rfind('*')
        next_first = ''.join(next).find('*')
        curr_last = ''.join(curr).rfind('*')
        curr_first = ''.join(curr).find('*')
        if curr_first > next_last:
            for i in range(next_last + 1, curr_first):
                screen[i][c] = "*"
        if curr_last < next_first:
            for i in range(curr_last + 1, next_first):
                screen[i][c + 1] = "*"
    return screen


lst = input().split()
W, H, A, B, func = int(lst[0]), int(lst[1]), int(lst[2]), int(lst[3]), lst[4]
show(graf(W, H, A, B, func))
