l = [int(x) for x in input().split()]

isValid = True

for i in l:
    if i > 100 or i < 0:
        print('잘못된 점수')
        isValid = False
        break
        
if isValid:
    if sum(l) / len(l) >= 80:
        print('합격')
    else:
        print('불합격')