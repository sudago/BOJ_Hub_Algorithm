from sys import stdin as s

n = int(s.readline())
m = int(s.readline())
INF = 1e9
graph = [[INF for _ in range(n+1)] for _ in range(n+1)] # 인접 행렬로 구성

for i in range(n+1):
    for j in range(n+1):
        if i == j: # 자기 자신은 0으로 초기화
            graph[i][j] = 0
            break;

for _ in range(m):
    a, b, c = map(int, s.readline().split())
    graph[a][b] = min(c, graph[a][b]) # 틀린이유: 노선이 하나가 아닐 수도 있음.

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], (graph[i][k] + graph[k][j])) # 최단 거리가 갱신되면 대입.

for i in range(1, n+1):
    result = " ".join(map(str, graph[i]))
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
