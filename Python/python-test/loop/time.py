# 2-3 time in three

def timeThree():
    sum = 0

    for min in range(60):
        for hour in range(24):
            if min == 3 or min == 13 or min == 23 or min == 33 or min == 43 or min == 53 \
                or hour == 3 or hour == 13 or hour == 23:
                sum += 1

    print(sum)
    print(sum * 60)

timeThree()