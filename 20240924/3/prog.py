lst = []
while s := input():
    lst.append(eval(s))
n = len(lst) // 2
lst1 = lst[:n]
lst2 = lst[n:]
res = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i][j] += lst1[i][k] * lst2[k][j]
for i in res:
    print(*i, sep=",")
                
