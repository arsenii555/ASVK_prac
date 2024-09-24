import string
lst1 = list(range(5, 16))
lst2 = list(string.ascii_lowercase)
lst2 = lst2[:lst2.index('k') + 1]
lst1[4:8] = lst2[-5:]
print(lst1)

