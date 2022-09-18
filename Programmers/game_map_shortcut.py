from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 주변이 벽으로 막혀 있어 상대 진영에 도착하지 못하는 경우
    # if n > 1 and m > 1:
    #     if maps[-1][-2] == 0 and maps[-2][-1] == 0:
    #         return -1
    # else:
    #     if n == 1 and maps[-1][-2] == 0:
    #         return -1
    #     if m == 1 and maps[-2][-1] == 0:
    #         return -1
    # bfs
    visited = [list(0 for _ in range(m)) for _ in range(n)]
    dq = deque([(0, 0)])
    visited[0][0] = 1
    while dq:
        x, y = dq.popleft()
        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:  # 남동북서
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0 or visited[nx][ny] > 0:  # 벽이거나 이미 방문
                continue
            dq.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    return visited[-1][-1] if visited[-1][-1] > 0 else -1
