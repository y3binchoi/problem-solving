N, K = map(int, input().split())
count = 0
for i in range(1, N + 1):
    if N % i == 0:  # N의 약수
        count += 1
    if count == K:  # K번째 약수
        print(i)
        break
else:
    print(0)  # N까지 해 봤는데 못찾음
