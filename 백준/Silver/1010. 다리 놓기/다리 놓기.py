from sys import stdin as s

limit = 30
dp = [1] * (limit+1)
for i in range(2, limit+1): # 팩토리얼 dp로 구현
    dp[i] = i * dp[i-1]

testcase = int(s.readline())
for _ in range(testcase):
    n, m = map(int, s.readline().split())
    result = dp[m] // (dp[n] * dp[m-n])  # 조합 공식: n개중에 순서 없이 r개를 고를 때, nCr = n! / r!(n-r)!
    print(result)