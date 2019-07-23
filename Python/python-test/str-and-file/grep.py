# 3-3 linux grep

def func():
    # find_str = input('grep string: ')
    # file_url = input('grep file url: ')
    find_str = 'if'
    file_url = 'C:\Studying\Python\python-test\str-and-file\caesar.py'

    f = open(file_url, mode='r', encoding='utf-8')
    i = 0

    for line in f:
        if find_str in line:
            print('{0}: {1}'.format(i+1, line))
        i += 1

func()