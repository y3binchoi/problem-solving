# 24416. 알고리즘 수업 - 피보나치 수 1
# 재귀 호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해보자.
# 재귀 호출 의사 코드
# fib(n) {
#     if (n = 1 or n = 2)
#     then return 1;  # 코드1
#     else return (fib(n - 1) + fib(n - 2));
# }
# 동적 프로그래밍 의사 코드
# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }

# 입력
n = int(input())


# 문제 해결
def fibo_recursive(n):
    global count_recursive
    if n == 1 or n == 2:
        count_recursive += 1
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def fibo_dp(n):
    global count_dp
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        count_dp += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


count_recursive = 0
count_dp = 0
fibo_recursive(n)
fibo_dp(n)

# 출력
print(count_recursive, count_dp)
