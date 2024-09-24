m, n = eval(input())
print([i for i in range(m, n) if not any(i % j == 0 for j in range(2, int(i ** 0.5) + 1)) and i != 1])

