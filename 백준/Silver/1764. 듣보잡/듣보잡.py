from sys import stdin as s

n, m = map(int, s.readline().rstrip().split())
dict = {}
count = 0
result = []

for _ in range(n+m):
    input = s.readline().rstrip()
    if input in dict:
        count += 1
        result.append(input)
    else:
        dict[input] = 1

print(count)
print("\n".join(sorted(result)))
