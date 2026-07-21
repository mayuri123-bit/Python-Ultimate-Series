# Match case is alternative of Switch-Case
value=2

match value:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("four")
    case _:
        print("invalid")