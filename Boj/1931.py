import sys

input = sys.stdin.readline
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: x[0])  # 시작시간으로 정렬
meeting.sort(key=lambda x: x[1])  # 종료시간으로 정렬
count = 1  # 일단 맨 왼쪽의 제일 빨리 끝나는 회의를 선택
pick = meeting[0][1]  # 선택한 회의의 끝나는 시간
for i in range(1, N):
    if meeting[i][0] >= pick:  # 시작 시간이 선택한 회의의 끝나는 시간 이후 이면
        count += 1
        pick = meeting[i][1]
print(count)
