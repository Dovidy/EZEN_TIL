# 2-5 Perfect Number

def count_perfNum(num:int):
    perf_list = []
    for i in range(1, num + 1):
        prime_list = []
        
        for j in range(1, int(i/2) + 1):
            if not (i % j):
                prime_list.append(j)
        
        if i == sum(prime_list):
            perf_list.append(i)
            # print(i)
            # print(prime_list)
            # print()

    return perf_list

print(count_perfNum(1000))