s = input().lower()
pairs = {s[i - 1] + s[i] for i in range(1, len(s)) if
         s[i].isalpha() and s[i - 1].isalpha()}
print(len(pairs))
