def break_and_continue(x: int, y: int) -> int:
    for i in range(2):
        if i == x:
            i = 3
            return i + 100
        elif i == y:
            i = 4
            break
        else:
            continue
    return i
