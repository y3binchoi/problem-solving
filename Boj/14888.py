import sys
from itertools import permutations

N = int(sys.stdin.readline())
operand = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

oper = '+' * operator[0] + '-' * operator[1] + '*' * operator[2] + '%' * operator[3]
cases = list(set(permutations(oper, N - 1)))
result = []
for case in cases:
    temp = operand[0]
    for i in range(1, N):
        if case[i - 1] == '+':
            temp += operand[i]
        elif case[i - 1] == '-':
            temp -= operand[i]
        elif case[i - 1] == '*':
            temp *= operand[i]
        elif case[i - 1] == '%':
            if temp > 0:  # 양수/양수
                temp //= operand[i]
            elif temp < 0:  # 음수/양수
                temp = (abs(temp) // operand[i]) * -1
    result.append(temp)
print(max(result))
print(min(result))
