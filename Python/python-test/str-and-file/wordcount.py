# 3-4 wordcount
from collections import Counter

def countWord(file_url:str):
    with open(file_url, 'r', encoding='utf-8') as f:
        words = [w.strip('.,') for w in f.read().split()]
        for w, c in Counter(words).most_common(10):
            print(w, c)
        
countWord('C:\Studying\Python\python-test\str-and-file\\test.txt')