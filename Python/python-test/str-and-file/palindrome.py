# 3-1. palindrome

def func():
    palin = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            num_str = str(i * j)
            half = int(len(num_str)/2)
            
            if len(num_str) % 2:
                if num_str[0:half] == num_str[-1:half:-1]:
                    palin.append([i*j, i, j])
            else:
                if num_str[0:half] == num_str[-1:half-1:-1]:
                    palin.append([i*j, i, j])
    
    return palin
            
a = func()

palin = [x[0] for x in a]
print(max(palin))