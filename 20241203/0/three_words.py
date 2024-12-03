class C:
    word1, word2, word3 = input().split()


while line := input():
    match line.split():
        case [C.word1, *tail] if "yes" in tail:
            print("case 1")
        case [C.word2]:
            print("case 2")
        case [C.word3, *mid, C.word2]:
            print("case 3")
        case _:
            print("default")