from sys import stdin as s

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = s.readline().rstrip()

for a in alpha:
    word = word.replace(a, 'a') # 크로아티아 문자 대체

print(len(word))
