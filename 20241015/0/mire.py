from collections import Counter
s1 = input().split()
s2 = input().split()
print((Counter(s2) - Counter(s1)) == Counter())

