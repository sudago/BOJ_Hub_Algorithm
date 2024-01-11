from sys import stdin as s

area = [[0 for _ in range(101)] for _ in range(101)] # 도화지 최대 넓이 설정
n = int(s.readline()) # 색종이 개수
length = 10
answer = 0

for _ in range(n):
    x, y = map(int, s.readline().rstrip().split())
    for i in range(x, x+length):
        for j in range(y, y+length):
            area[i][j] = 1 # 넓이 1씩 할당하기

for a in area:
    answer += sum(a) # 넓이를 모두 더하기

print(answer)