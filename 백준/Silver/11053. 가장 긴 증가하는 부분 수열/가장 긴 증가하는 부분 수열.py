from sys import stdin as s

n = int(s.readline())
a = list(map(int, s.readline().rstrip().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))