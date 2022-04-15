import sys

N, M = map(int, sys.stdin.readline().split())
rec = [sys.stdin.readline().strip() for _ in range(N)]
maxSize = 1
for x1 in range(N):
    for y1 in range(M - 1):
        for y2 in range(y1 + 1, M):  # 중복 없이 2개 선택
            side = y2 - y1
            x2 = x1 + side
            if x2 < N:  # 행의 인덱스 0~N-1
                if rec[x1][y1] == rec[x1][y2] == rec[x2][y1] == rec[x2][y2]:  # 정사각형
                    maxSize = max(maxSize, (side + 1) ** 2)
print(maxSize)
