def isPalindorme(a):
    for i in range(len(a) // 2):
        if a[i] != a[-1-i]:
            return False
    return True

with open(r'C:\SmartData\TIL_EZEN\Python\python-dojang\unit22-29\words2.txt', 'r', encoding='utf-8') as file:
    for line in file:
        word = line.strip('\n')
        if isPalindorme(word):
            print(word)