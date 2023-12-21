from sys import stdin as s

while True:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = s.readline().rstrip().lower()
    if word == '#':
        break;
    for i in word:
        if i in vowels:
            count += 1
    print(count)