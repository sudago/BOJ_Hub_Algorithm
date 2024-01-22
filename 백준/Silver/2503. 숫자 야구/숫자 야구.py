import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())

nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(permutations(nums, 3))

for _ in range(N):
    n, s, b = map(int, sys.stdin.readline().split())
    n = list(str(n))
    rmcnt = 0 # 순열 배열에서 요소 삭제 시, index 0번째 부터 다시 비교하기 위한 cnt
    for i in range(len(num)):
        strike = ball = 0
        i -= rmcnt
        for j in range(3):
            if num[i][j] == n[j]:
                strike += 1
            elif n[j] in num[i]:
                ball += 1
        if strike != s or ball != b:
            num.remove(num[i])
            rmcnt += 1

print(len(num))
