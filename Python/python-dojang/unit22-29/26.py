(_a , _b) = (int(i) for i in input().split())

a = set(i for i in range(1, _a + 1) if _a % i == 0)
b = set(i for i in range(1, _b + 1) if _b % i == 0)

divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)