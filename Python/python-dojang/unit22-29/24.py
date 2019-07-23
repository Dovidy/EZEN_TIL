import re

# inp = input()
input_str = '''the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.'''

#regex = re.compile(r'[^a-zA-z]the[^a-zA-z]') # 'the' 를 캐치못함
regex = re.compile(r'\b(the)\b')
m = regex.findall(input_str)

print(m)
print(len(m))