from sys import stdin as s
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        now = q.popleft()
        for a in arr[now]:
            if visited[a] == 0: # 방문한적이 없으면
                visited[a] = visited[now] + 1
                q.append(a)


n = int(s.readline())
start, end = map(int, s.readline().rstrip().split())
m = int(s.readline())
arr = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, s.readline().rstrip().split())
    arr[x].append(y) # 양방향 연결
    arr[y].append(x)

bfs(start)

if visited[end] == 0: 
    print(-1)
else:
    print(visited[end] - 1) # 방문 표시를 위해 맨 처음 +1했던 값을 빼준다.