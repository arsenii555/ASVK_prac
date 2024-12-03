while line := input():
    match line.split():
        case ["mov", r1, r2]:
            print(f"moving {r2} to {r1}")
        case [("push" as cmd) | ("pop" as cmd), *reglist]:
            print(f"{cmd}ing", *reglist)
        case [cmd, r1]:
            print(f"making {cmd} with {r1}")
        case _:
            print("ParseError")
