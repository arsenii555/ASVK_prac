a, b = eval(input())
print([i for i in range(a, b) if '3' not in str(i) and i % 2])
