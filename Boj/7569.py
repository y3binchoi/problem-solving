# 7569. 토마토(3차원)
import sys
from collections import deque

# 입력
# 상자 가로 M, 세로 N, 쌓인 상자 수 H
input = sys.stdin.readline
M, N, H = map(int, input().split())
boxes = [list() for _ in range(H)]

# bfs(상자 번호, 행, 열)
deq = deque([])
diff = [
    (-1, 0, 0), (1, 0, 0),  # 앞뒤
    (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)  # 상하좌우
]
for h in range(H):  # H 상자
    for x in range(N):
        row = list(map(int, input().split()))
        boxes[h].append(row)
        for y in range(M):
            if row[y] == 1:
                deq.append((h, x, y))
while deq:
    h, x, y = deq.popleft()
    for dh, dx, dy in diff:
        nh = dh + h
        nx = dx + x
        ny = dy + y
        if nh < 0 or nh >= H or nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if boxes[nh][nx][ny] == 0:  # 안익은 토마토
            boxes[nh][nx][ny] = boxes[h][x][y] + 1
            deq.append((nh, nx, ny))

# 출력
ripen = True
days = -1
for h in range(H):
    for x in range(N):
        for y in range(M):
            if boxes[h][x][y] == 0:
                print(-1)
                exit(0)
        days = max(days, max(boxes[h][x]))
print(days - 1)
