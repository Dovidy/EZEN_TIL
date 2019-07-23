import string
import os


with open(r'C:\SmartData\TIL_EZEN\Python\python-dojang\unit22-29\words.txt', 'r', encoding='utf-8') as file:
    words = file.readline().split()
    for word in words:
        if word.find('c') >= 0:
            word = word.strip(string.punctuation)
            print(word)