from collections import deque
from sys import stdin

# 시험관 크기 n*n 바이러스 번호 1~k
# s초후 (r-1,c-1)위치의 바이러스 출력
input = stdin.readline
n, k = map(int, input().split())
test_tube = [list(map(int, input().split())) for _ in range(n)]
s, r, c = map(int, input().split())

# bfs
# 큐에 (바이러스 번호, 행, 열)으로 저장
dq = deque()
temp = []
for i in range(n):
    for j in range(n):
        if test_tube[i][j] == 0:
            continue
        temp.append((test_tube[i][j], i, j))
temp.sort()
dq.extend(temp)
for _ in range(s):
    temp = []
    while dq:
        num, x, y = dq.popleft()
        for nx, ny in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if test_tube[nx][ny] > 0:
                continue
            temp.append((num, nx, ny))
            test_tube[nx][ny] = num
    dq.extend(temp)

print(test_tube[r - 1][c - 1])