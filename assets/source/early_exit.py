def early_exit(a: int) -> int:
    c = 0
    while c < 10:
        c += 3
        if c > a:
            return c + 1
    return c
