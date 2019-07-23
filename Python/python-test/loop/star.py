# 2-2 diamond star

def drawStar(num:int):
    up = int(num/2) + 1
    low = int(num/2)
    
    for i in range(up+1):
        for j in range(up - i):
            print(' ', end='')
        for j in range(i * 2 - 1):
            print('*', end='')
        print()
    
    for i in range(low, 0, -1):
        for j in range(low - i + 1):
            print(' ', end='')
        for j in range(i * 2 - 1):
            print('*', end='')
        print()
    
#drawStar(int(input()))
drawStar(7)