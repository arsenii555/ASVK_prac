lst = list(map(int, input().split(",")))
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j] ** 2 % 100 > lst[j + 1] ** 2 % 100:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)
