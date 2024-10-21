w = int(input())
words = {}
while line := input():
    for sym in """.,:;!?-0123456789\'\"""":
        line = line.replace(sym, " ")
    line_split = line.lower().split()
    for word in line_split:
        if len(word) == w:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

res = sorted(words.items(), key=lambda x: (-x[1], x[0]))
if res:
    max_freq = res[0][1]
    print(*map(lambda x: x[0], filter(lambda x: x[1] == max_freq, res)))



