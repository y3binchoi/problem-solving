# 14503. 로봇 청소기
import sys
from collections import deque

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def turn_left(now):
    new = (now+3) % 4
    return new


def go_back(x, y, now_d):
    nx = x-dr[now_d]
    ny = y-dc[now_d]
    return nx, ny


input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
visited[r][c] = 1
cnt = 1  # 청소 영역 카운트
while True:
    flag = 0
    for _ in range(4):
        d = turn_left(d)
        nr = r+dr[d]
        nc = c+dc[d]
        if nr < 0 or nr > N-1 or nc < 0 or nc > M-1:
            continue
        if area[nr][nc] != 0 or visited[nr][nc] != 0:
            continue
        cnt += 1
        visited[nr][nc] = cnt
        r, c = nr, nc
        flag = 1
        break  # 청소 한 방향으로 전진
    if flag == 0:  # 4방향 모두 청소가 되어 있음
        r_back, c_back = go_back(r, c, d)
        if area[r_back][c_back]:  # 후진 했는데 벽
            print(cnt)
            break
        else:
            r, c = r_back, c_back

# print(*area, sep='\n')
# print(*visited, sep='\n')
