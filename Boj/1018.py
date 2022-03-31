import sys

WB = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
BW = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
N, M = map(int, sys.stdin.readline().split())
chessboard = list(sys.stdin.readline().rstrip() for _ in range(N))
num_of_case_n = N - 8  # 세로 경우의 수
num_of_case_m = M - 8  # 가로 경우의 수
repaint = []  # 다시 칠해야 하는 네모 갯수


def countRepaint(row, col):
    wb_count = 0
    bw_count = 0
    for i in range(8):
        for j in range(8):
            if chessboard[row + i][col + j] != WB[i][j]:
                wb_count += 1
            if chessboard[row + i][col + j] != BW[i][j]:
                bw_count += 1
    repaint.append(wb_count)
    repaint.append(bw_count)


if num_of_case_n or num_of_case_m:
    for n in range(num_of_case_n + 1):  # 판의 세로를 자르는 행위
        for m in range(num_of_case_m + 1):  # 판의 가로를 자르는 행위
            countRepaint(n, m)
else:  # 8x8
    countRepaint(0, 0)
print(min(repaint))
