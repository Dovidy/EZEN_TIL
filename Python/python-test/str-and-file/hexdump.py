# 3-6 Hexadump

import binascii

with open('C:\Studying\Python\python-test\str-and-file\\bin.p', 'rb') as f:
	t = f.read()
	tt = binascii.hexlify(t)
	print(tt[:60])