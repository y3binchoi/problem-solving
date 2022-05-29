# 16928. 뱀과 사다리 게임
from collections import deque

# 입력
# 사다리 수 N, 뱀의 수 M
N, M = map(int, input().split())
ladder = dict()  # 사다리 정보 받기
for n in range(N):
    start, end = map(int, input().split())
    ladder[start] = end
snake = dict()  # 뱀 정보 받기
for m in range(M):
    start, end = map(int, input().split())
    ladder[start] = end

# bfs(현재칸)
board = [0] * 101  # 방문 체크
deq = deque([])
deq.append(1)
while deq:
    now = deq.popleft()
    if board[100] != 0:  # 도착
        break
    for dice in range(1, 7):
        move = now + dice
        if move > 100:  # 판 바깥
            continue
        if move in ladder.keys():  # 사다리 타고 이동
            move = ladder[move]
        # if move in snake.keys():  # 사실 빨리 가야 하니까 뱀은 타면 안됨.
        #     move = snake[move]
        if board[move] != 0:  # 이미 방문
            continue
        board[move] = board[now] + 1
        deq.append(move)

# 출력
print(board[100])