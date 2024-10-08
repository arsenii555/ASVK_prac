from math import *


def scale(a, b, A, B, x):
    return (x - a) / (b - a) * (B - A) + A


def lazy_plot(H, W, A, B):
    plot = [[" "] * W for i in range(H)]
    X = [A + (B - A) / H * i for i in range(H)]
    X_scaled = list(map(lambda x: int(scale(A, B, 0, H - 1, x)), X))
    Y = list(map(lambda x: sin(x), X))
    Y_scaled = list(map(lambda y: int(scale(-1, 1, 0, W - 1, y)), Y))
    for x, y in zip(X_scaled, Y_scaled):
        plot[x][y] = '*'
    for i in range(H):
        if plot[i].count('*') > 1:
            indexes = [i for i, x in enumerate(plot[i]) if x == '*']
            for j in range(indexes[0], indexes[-1]):
                plot[i][j] = "*"
    for i in range(1, H):
        prev_last_star = ''.join(plot[i - 1]).rfind('*')
        curr_last_star = ''.join(plot[i]).rfind('*')
        prev_first_star = ''.join(plot[i - 1]).find('*')
        curr_first_star = ''.join(plot[i]).find('*')
        if curr_first_star > prev_last_star:
            plot[i - 1][prev_last_star + 1: prev_last_star + (curr_last_star - prev_last_star) // 2 + 1] = (
                    ["*"] * ((curr_last_star - prev_last_star) // 2 - 1))
            plot[i][prev_last_star + (curr_last_star - prev_last_star) // 2: curr_last_star] = (
                    ['*'] * ((curr_last_star - prev_last_star) // 2 - 1))
        elif curr_last_star < prev_first_star:
            plot[i - 1][curr_last_star + (prev_first_star - curr_last_star) // 2 + 1: prev_first_star] = ['*'] * ((
                        prev_first_star - curr_last_star) // 2)
            plot[i][curr_last_star + 1: curr_last_star + (prev_first_star - curr_last_star) // 2 + 1] = ['*'] * ((
                        prev_first_star - curr_last_star) // 2)
    for i in range(H):
        print(*plot[i])


lazy_plot(60, 20, -10, 10)
