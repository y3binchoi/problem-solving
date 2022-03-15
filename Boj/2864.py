data = list(input().split())
maximum = 0
minimum = 0

for n in data:
    maximum += int(n.replace('5', '6'))
    minimum += int(n.replace('6', '5'))

print(minimum, maximum)
