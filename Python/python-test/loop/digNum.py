def count_dig(start:int, end:int):
    dig_arr = {i:0 for i in range(0, 10)}

    for i in range(start, end + 1):
        for j in str(i):
            dig_arr[int(j)] += 1

    print(dig_arr)


count_dig(1, 1000)