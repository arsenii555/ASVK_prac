def digit_sum(n):
    res = 0
    while n:
        res += n % 10
        n //= 10
    return res

        
n = int(input())
i = n
j = n
while i < n + 3:
    while j < n + 3:
        print(i, "*", j, "=", (i * j if digit_sum(i * j) != 6 else ":=)"), end=" ")
        j += 1
    print()
    i += 1
    j = n

