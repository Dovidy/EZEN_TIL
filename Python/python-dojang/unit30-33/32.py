files = input().split()

print(list(map(lambda f: '{0:03d}.{1}'.format(int(f.split('.')[0]), f.split('.')[1]), files)))