N = int(input())
Pi = list(map(int, input().split()))
Pi.sort()
timeTaken = 0
temporary = []

for p in range(N):
    temporary = Pi[:p + 1]
    timeTaken += sum(temporary)

print(timeTaken)
