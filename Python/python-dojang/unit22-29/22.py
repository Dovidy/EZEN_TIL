(start, end) = (int(x) for x in input().split())
li = []

for i in range(start, end + 1):
    li.append(2 ** i)

del li[1]
del li[-2]

print(li)