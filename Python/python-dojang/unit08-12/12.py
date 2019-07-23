# 12.5 

keys = input().split()
vals = input().split()

dic = {}

for i in range(len(keys)):
    dic[keys[i]] = vals[i]

print(dic)