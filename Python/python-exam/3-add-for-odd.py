[a, b] = [int(i) for i in input().split()]

sum = 0
for i in range(a, b+1):
    if i % 2:
        sum += i

print(sum)