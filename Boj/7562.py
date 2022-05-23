# 7562. 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    # 입력
    I = int(input())  # 체스판 크기 IxI
    now_x, now_y = map(int, input().split())  # 현재 위치
    move_x, move_y = map(int, input().split())  # 이동하고 싶은 위치

    # bfs
    diff = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    chessboard = [[0] * I for _ in range(I)]

    deq = deque([(now_x, now_y)])
    while deq:
        x, y = deq.popleft()
        if x == move_x and y == move_y:  # 찾음
            break
        for dx, dy in diff:
            newx = dx + x
            newy = dy + y
            if 0 <= newx < I and 0 <= newy < I:
                if chessboard[newx][newy] == 0:  # 0 방문한 적 없는 칸
                    deq.append((newx, newy))
                    chessboard[newx][newy] = 1 + chessboard[x][y]

    # 출력
    print(chessboard[move_x][move_y])
    # print(*chessboard, sep='\n')
