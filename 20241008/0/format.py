max_len = 3 + len(bin(23)) + len(hex(23))
for i in range(12, 24):
    print(f"{bin(i)} {'=': <{(max_len - len(bin(i)) - len(hex(i))) - 1}}{hex(i)}")
