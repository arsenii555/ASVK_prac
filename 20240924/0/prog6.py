matrix = []
while s := input():
    matrix.append(eval(s))
n = len(matrix)
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in matrix:
    print(i)