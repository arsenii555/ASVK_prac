s = 0
while (i := int(input())) > 0:
    if i <= 0:
        break
    s += i
    if s > 21:
        print(s)
        break
else:
    print(i)
