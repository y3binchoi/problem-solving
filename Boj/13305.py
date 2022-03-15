N = int(input())
distance = list(map(int, input().split()))
price_per_L = list(map(int, input().split()))

min_price = price_per_L[0]
minimumCost = 0

for n in range(N - 1):
    if price_per_L[n] < min_price:
        min_price = price_per_L[n]
    minimumCost += min_price * distance[n]

print(minimumCost)
