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

pal_list = [x[0] for x in palin]
max_palin, x, y = palin[pal_list.index(max(pal_list))]
print(max_palin, ((x, y) if (x < y) else (y, x)))
