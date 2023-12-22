from sys import stdin as s

n = int(s.readline())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, s.readline().split())) # 인접 행렬이 주어진다.

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]: # 2에서 1번 노드로 가는 길을 지나고, 1에서 3번 노드로 가는 길을 지났디면
                graph[i][j] = 1 # 2에서 3번 노드로 가는 길도 방문 가능 하므로 방문 처리 하기.
            
for row in graph:
    print(" ".join(map(str, row)))