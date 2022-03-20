import sys

input = sys.stdin.readline
expr = input().strip()  # 공백 제거 해서 마지막 \n없이 받음
answer = 0
isMinus = 0
buffer = ''

for c in expr:
    if c == '+':
        if isMinus:
            answer -= int(buffer)
        else:
            answer += int(buffer)
        buffer = ''
    elif c == '-':
        if isMinus:
            answer -= int(buffer)
        else:
            answer += int(buffer)
        isMinus = 1
        buffer = ''
    else:  # 숫자인 경우
        buffer += c  # 문자열 그대로 붙이기
else:  # 마지막 수 까지 계산
    if isMinus:
        answer -= int(buffer)
    else:
        answer += int(buffer)

print(answer)