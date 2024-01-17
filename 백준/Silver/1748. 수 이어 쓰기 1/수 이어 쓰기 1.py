from sys import stdin as s

n = int(s.readline())
if 1 <= n <= 9:
    print(n)
    exit()

length = len(str(n))
answer = 11 # 10은 11개
for i in range(2, length+1):
    if i < length:
        # n이 3자리 수라면 11 ~ 100까지 글자 수를 더해주는 작업.
        # (2자리 수 중 가장 큰 수 - (이미 answer에 들어있는 10까지의 글자 수)) * 2자리 수 + 3자리 수
        # ((100 - 1) - 10) * 2 + 3
        answer += ((10**i - 1) - 10**(i-1)) * i + (i+1)
        continue
    answer += (n - 10**(i-1)) * i
print(answer)