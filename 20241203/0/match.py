t = b"qweas"
match t.split():
    case []:
        print("empty")
    case ["qwe"]:
        print("No doubt qwe")
    case [str(x)]:
        print("List of 1 str")
    case [x]:
        print("List of 1 elem")
