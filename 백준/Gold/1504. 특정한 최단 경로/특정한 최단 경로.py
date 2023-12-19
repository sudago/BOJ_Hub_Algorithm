from sys import stdin as s
import heapq

def dijkstra(start):
    distance = [INF for _ in range(N+1)] # 실패 이유: distance를 함수 바깥에 뒀다.
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 방문했으면서 더 비용이 적은 거리를 구했다면
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]: # 더 비용이 적게 계산이 되었다면
                distance[i[0]] = cost # 최단거리 갱신
                heapq.heappush(q, [cost, i[0]])
    return distance


N, E = map(int, s.readline().rstrip().split()) # 정점 개수와 간선 개수
graph = [[] for _ in range(N+1)]
INF = 1e9

for _ in range(E):
    a, b, c = map(int, s.readline().rstrip().split()) # 노드, 노드, 가중치(비용)
    graph[a].append([b, c]) # 양방향 연결을 해준다.
    graph[b].append([a, c])

v1, v2 = map(int, s.readline().rstrip().split())

original_distance = dijkstra(1)
v1_distance = dijkstra(v1) # v1를 시작으로 최단 거리를 다시 구한다.
v2_distance = dijkstra(v2) # v2를 시작으로 최단 거리를 다시 구한다.
# 1부터 v1까지의 최단 거리 + v1과 v2 사이의 간선의 비용 + v2부터 N까지의 최단 거리
total_distance1 = original_distance[v1] + v1_distance[v2] + v2_distance[N]
# 1부터 v2까지의 최단 거리 + v1과 v2 사이의 간선의 비용 + v1부터 N까지의 최단 거리
total_distance2 = original_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(total_distance1, total_distance2)

if result >= INF:
    print(-1)
else:
    print(result)
