vegatables = {'가지':800, '오이':600, '수박':15000, '호박':1000, '깻잎':500}

veg_sort_keys = sorted(vegatables, key=lambda k: vegatables[k], reverse=True)

for veg in veg_sort_keys:
    print(f'{veg}: {vegatables[veg]:7,}')