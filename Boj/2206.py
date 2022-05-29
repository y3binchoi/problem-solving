# 2206. 벽 부수고 이동하기
import sys
from collections import deque

# 입력
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

# bfs(x,y)
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # visited[x][y][벽부수기가능0 or 벽이미부숨1]

q = deque([(0, 0, 0)])
visited[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    if visited[N - 1][M - 1][0]:  # 벽 안뚫고 끝에 도착
        print(visited[N - 1][M - 1][0])
        break
    if visited[N - 1][M - 1][1]:  # 벽 뚫고 끝에 도착
        print(visited[N - 1][M - 1][1])
        break
    for dx, dy in diff:
        nx = dx + x
        ny = dy + y
        if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 맵 밖
            continue
        # 다음 칸이 벽이고, 아직 벽 부수기를 하지 않은 경우
        if graph[nx][ny] == 1 and z == 0:
            visited[nx][ny][1] = visited[x][y][0] + 1
            q.append((nx, ny, 1))
        # 다음 칸이 벽이 아니고, 아직 한 번도 방문하지 않은 곳
        elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
            visited[nx][ny][z] = visited[x][y][z] + 1
            q.append((nx, ny, z))
else:
    print(-1)
# 디버깅
# print(*visited, sep='\n')
