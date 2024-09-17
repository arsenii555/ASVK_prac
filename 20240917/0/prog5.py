while s := input():
    n = eval(s)
    if n == 13:
        break 
    if not n % 2:
        print(n)
else:
    print("Congratulations!")

