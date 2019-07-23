def isLeap(num:int):
    return not not (not (num % 4) and ((num % 100) or not (num % 400)))