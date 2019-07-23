# 2-6. sum of square, square of sum 

def func(num:int):
    sum_of_squared = 0
    square_of_sum = sum(list(range(1, num+1))) ** 2
    
    for i in range(1, num+1):
        sum_of_squared += i ** 2
    
    return square_of_sum - sum_of_squared


print(func(10))