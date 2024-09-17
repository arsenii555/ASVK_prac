a = int(input())
match a:
    case 1:
        print("один")
    case 2:
        print("два")
    case 3:
        print("три")
    case var if var % 2:
        print("N -- это много")
    case _: 
        print("чётное")
         
