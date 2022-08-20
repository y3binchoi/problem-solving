# 소수&팰린드롬
# 문제
# 어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부른다. 예를 들어 79,197과 324,423 등이 팰린드롬 수이다.
# 어떤 수 N (1 ≤ N ≤ 1,000,000)이 주어졌을 때, N보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서, 가장 작은 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다.

# 출력
# 첫째 줄에 조건을 만족하는 수를 출력한다.

import math
from sys import stdin
input = stdin.readline


def is_prime_number(x):  # 시간 복잡도 O(N^(1/2))
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False  # 소수 아님
    return True  # 소수


def is_palindrome(x):
    str_x = str(x)
    for i in range(len(str_x)//2):
        if str_x[i] != str_x[-i-1]:
            return False  # 펠린드롬 아님
    return True  # 펠린드롬


n = int(input())
while True:
    if is_palindrome(n) and is_prime_number(n):
        break
    n += 1
print(n)
