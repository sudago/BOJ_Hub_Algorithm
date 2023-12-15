from sys import stdin as s
from collections import deque

def bfs(graph, dist, a, b):
    q = deque()
    q.append((a, b))
    dist[a][b] == 1 # 방문처리
    while q: # q가 빌때까지
        x, y = q.popleft()
        nx = [x-1, x-1, x, x+1, x+1, x+1, x, x-1]
        ny = [y, y+1, y+1, y+1, y, y-1, y-1, y-1]
        for i in range(8): # 북 북동 동 남동 남 남서 서 북서
            dx, dy = nx[i], ny[i]
            # 범위 내에 있으면서, 땅이면서, 방문한 적이 없다면
            if 0 <= dx < h and 0 <= dy < w and graph[dx][dy] == 1 and dist[dx][dy] == 0:
                dist[dx][dy] = 1 # 방문처리
                q.append((dx, dy))


while True:
    w, h = map(int, s.readline().rstrip().split())
    if (w == 0 and h == 0): # 테스트 케이스 끝
        break
    dist = [[0 for _ in range(w)] for _ in range(h)]
    graph = []
    answer = 0
    for _ in range(h):
        row = list(map(int, s.readline().rstrip().split()))
        graph.append(row)
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and dist[i][j] == 0: # 땅이면서 방문하지 않았다면
                bfs(graph, dist, i, j)
                answer += 1
    
    print(answer)
