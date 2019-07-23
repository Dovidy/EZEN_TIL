# 2-1 sum of input

def calc_sum():
    test_num = int(input())

    arr = []
    for i in range(test_num):
        arr.append(input())
        
    for i in range(test_num):
        (a, b) = arr[i].split(' ')
        print('Case #{0}: {1} + {2} = {3}'.format(i+1, a, b, int(a) + int(b)))

calc_sum()