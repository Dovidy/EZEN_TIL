bond = int(input())

origin = 10
after = origin
year = 0

while True:
    if after > 2 * origin:
        print(year, after)
        break

    after = after * ((bond / 100) + 1)
    year += 1
    print(year, after)

print(year)