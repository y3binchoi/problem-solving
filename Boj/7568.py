import sys

N = int(sys.stdin.readline())
build = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

rank = [0 for _ in range(N)]  # 덩치 등수

for i in range(N - 1):
    for j in range(i + 1, N):
        if build[i][0] < build[j][0] and build[i][1] < build[j][1]:
            rank[i] += 1  # i가 j보다 덩치가 작은 경우 i등수+1
        elif build[i][0] > build[j][0] and build[i][1] > build[j][1]:
            rank[j] += 1  # i가 j보다 덩치가 큰 경우 j등수+1
for r in range(N):
    print(rank[r] + 1, end=' ')
