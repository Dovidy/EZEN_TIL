def counter(n):
    i = n + 1
    def count():
        nonlocal i
        i -= 1
        return i
    return count

n = int(input())

c = counter(n)
for i in range(n):
    print(c(), end=' ')