N = int(input())
count = -1

m5 = [5 * i for i in range((N // 5) + 1)]  # 0, 5, 10, ... , n보다 작은 5의 배수
m3 = [3 * i for i in range((N // 3) + 1)]  # 0, 3, 6, ... , n보다 작은 3의 배수

for n5 in reversed(m5):
    for n3 in reversed(m3):
        sum_n = n5 + n3
        if sum_n < N:
            break
        elif sum_n == N:
            count = m5.index(n5) + m3.index(n3)
            break
    if count != -1:
        break

print(count)
