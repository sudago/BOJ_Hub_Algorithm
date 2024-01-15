from sys import stdin as s

n, m = map(int, s.readline().rstrip().split())
rectangle = [list(map(int, list(s.readline().rstrip()))) for _ in range(n)]

answer = 1
for i in range(n):
    for j in range(m):
        now = rectangle[i][j]
        for y in range(j+1, m):
            if now == rectangle[i][y]: # 가로부터 탐색 (정사각형의 윗쪽 꼭짓점 두 개 확인)
                x = i + (y-j) # 현재 row + 길이
                if x <= 0 or n <= x: # 직사각형의 범위를 초과한다면 3번째 반복문 탈출
                    break;
                if now == rectangle[x][j] == rectangle[x][y]: # 4개의 꼭짓점의 값이 일치한다면
                    area = (y-j+1)**2 # y-j는 index값이므로 +1을 해서 실제 변의 길이로 만들어 준다.
                    answer = max(answer, area) # 정사각형의 최대 넓이 갱신

print(answer)