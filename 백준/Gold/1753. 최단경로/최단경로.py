# 1753번, 최단경로
import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().rstrip().split()) # 정점의 개수, 간선의 개수
K = int(input())  # 시작 정점
graph = [[] for _ in range(V+1)]
INF = int(1e9)
distance = [INF] * (V+1)

for _ in range(E):
    u, v, m = map(int, input().rstrip().split())
    graph[u].append((v, m))  # (연결된 정점, 비용)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 계산된 거리, 현재 정점
        if distance[now] < dist:  # 거리 기준으로 오름차 순 정렬해서 최단거리를 계산했으므로, q에 먼저 넣었어도 나중에 계산될 수 있다.
            continue
        for next, cost in graph[now]:  # 현재 노드와 연결된 노드 순회
            total_cost = dist + cost
            if distance[next] > total_cost:  # 최단 거리 갱신
                distance[next] = total_cost
                heapq.heappush(q, (total_cost, next))

dijkstra(K)

for i in range(1, V+1):
    print('INF' if distance[i] == INF else distance[i])

