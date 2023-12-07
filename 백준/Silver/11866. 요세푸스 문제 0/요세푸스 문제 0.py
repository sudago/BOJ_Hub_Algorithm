from sys import stdin as s
from collections import deque

N, K = map(int, s.readline().rstrip().split()) # 인원 수, K번째 사람
nums = deque([i for i in range(1, N+1)])
answer = []

while len(nums) != 0:
    for _ in range(K-1):
        nums.append(nums.popleft())
    answer.append(nums.popleft())

print("<", end="")
for i in range(N):
    print(answer[i], end="")
    if i < N-1:
        print(", ", end="")
print(">")