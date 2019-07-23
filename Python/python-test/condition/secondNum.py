def second_bigger_num(a:int, b:int, c:int):
    if a > b:
        if c > b:
            if a > c:
                return c
            else:
                return a
        else:
            return b
    else:
        if a > c:
            return a
        else:
            if b > c:
                return c
            else:
                return b
