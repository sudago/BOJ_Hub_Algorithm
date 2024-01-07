from collections import defaultdict

dic = defaultdict(int)

word = input()
for ch in word:
    ch = ch.lower()
    dic[ch] += 1

arr = []
max_num = max(dic.values())
for key in dic:
    if max_num == dic[key]:
        arr.append(key)

if 1 < len(arr):
    print('?')
else:
    print(arr[0].upper())