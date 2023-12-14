from sys import stdin as s
from collections import deque

def bfs(graph, dist, n):
    q = deque()
    q.append(n)
    while q: # queue가 빌 때까지
        i = q.popleft()
        if dist[i] == 0: # 방문하지 않았다면
            for j in range(len(graph[i])):    
                if graph[i][j] == 1: # 연결 되어있다면
                    q.append(j)
        dist[i] = 1 # 방문 처리
    return sum(dist) - 1  # 자기 자신 제외하고 방문 count


n = int(s.readline()) # 컴퓨터 수 (node)
m = int(s.readline()) # 연결된 컴퓨터 수 (edge)
graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # 인접 행렬을 만든다.
dist = [0 for _ in range(n+1)] # 방문 처리
answer = 0

for _ in range(m): # 입력 값
    a, b = map(int, s.readline().split())
    graph[a][b], graph[b][a] = 1, 1 # 연결 시켜주기

answer = bfs(graph, dist, 1)

print(answer)