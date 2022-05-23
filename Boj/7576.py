# 7576. 토마토
import sys
from collections import deque

# 입력
input = sys.stdin.readline
m, n = map(int, input().split())  # 토마토 행렬 NxM
box = [list(map(int, input().split())) for _ in range(n)]

# bfs
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
deq = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:  # 익은 토마토 확인
            deq.append((i, j))
while deq:
    x, y = deq.popleft()
    for dx, dy in diff:
        nx = dx + x
        ny = dy + y
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if box[nx][ny] == 0:  # 안 익은 토마토
            deq.append((nx, ny))
            box[nx][ny] = box[x][y] + 1

# 출력
# print(*box, sep='\n')
ripen = True  # 다 익었는지
days = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            ripen = False
            break
    days = max(max(box[i]), days)
days -= 1  # 1일부터 n일: n-1일 걸린 것.
print(-1 if not ripen else days)
