# 3-2. caesar crypt

def caesar(passwd:str, num:int):
    crypt = ''
    for alp in passwd:
        if alp >= 'a' and alp <= 'z':
            crypt += chr((ord(alp) - ord('a') + num) % 26 + ord('a'))
        elif alp >= 'A' and alp <= 'Z':
            crypt += chr((ord(alp) - ord('A') + num) % 26 + ord('A'))
        elif alp >= '0' and alp <= '9':
            crypt += chr((ord(alp) + num) % 10)
        else:
            crypt += alp
        
    return crypt

print(caesar('rose', 5)) 
print(caesar('come to rome', 3))