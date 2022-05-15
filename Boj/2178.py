import sys
from collections import deque

# NxM 행렬 입력
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# 상 하 좌 우
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 문제 해결: BFS
def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    while deq:
        x, y = deq.popleft()
        for dx, dy in diff:
            newx = dx + x
            newy = dy + y
            if 0 <= newx < n and 0 <= newy < m:  # 미로 인덱스 범위
                if maze[newx][newy] == 1:  # 벽(0)이 아니며, 가보지 않은 길
                    deq.append((newx, newy))
                    maze[newx][newy] = maze[x][y] + 1
    return maze[n - 1][m - 1]


# 출력
print(bfs(0, 0))
