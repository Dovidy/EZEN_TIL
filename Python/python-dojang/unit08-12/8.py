def isSatisfied(input:str):
    (kor, eng, math, science) = map(int, input.split(' '))
    if kor >= 90 and eng > 80 and math > 85 and science >= 80:
        return True
    else:
        return False

# print(isSatisfied('90 81 86 80'))
# print(isSatisfied('90 80 85 80'))
print(isSatisfied(input()))