payment = int(input())
received = 1000
change = [500, 100, 50, 10, 5, 1]
count = 0

received -= payment
for coin in change:
    count += received // coin
    received = received % coin

print(count)
