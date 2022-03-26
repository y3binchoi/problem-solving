import sys

N = int(sys.stdin.readline())

constructor = 0  # 생성자
decompose = 0  # 분해합
start = N - 54  # 생성자로 고려 해볼 최솟값
if start < 0:
    start = 0

for c in range(start, N):
    constructor = c
    decompose = 0  # 새로 계산할 때 초기화 필요
    for i in str(c):  # 각 자리수 더하기
        decompose += int(i)
    decompose += c
    if decompose == N:  # 찾음
        break
    else:
        constructor = 0

print(constructor)
