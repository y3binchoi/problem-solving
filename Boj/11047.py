N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
count = 0

for c in reversed(coins):
    count += K // c
    K = K % c

print(count)
