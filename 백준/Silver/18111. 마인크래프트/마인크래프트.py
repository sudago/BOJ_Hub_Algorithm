import sys
INF = sys.maxsize

N, M, B = map(int, sys.stdin.readline().rstrip().split(" "))

minecraft = []
for _ in range(N):
    minecraft.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

sec = INF
for i in range(257):
    one = two = 0
    for j in range(N):
        for k in range(M):
            if minecraft[j][k] < i:
                one += i - minecraft[j][k]
            else:
                two += minecraft[j][k] - i

    if one > two + B:
        continue

    if one+two*2 <= sec:
        sec = one+two*2
        height = i

print(sec, height)