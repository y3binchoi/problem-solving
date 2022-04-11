N = 9
cm = [int(input()) for _ in range(N)]
dwarf = [1 for _ in range(N)]  # 드워프 맞으면 1 아니면 0
sum_cm = sum(cm)
cm.sort()
for i in range(N - 1):
    for j in range(i + 1, N):
        if sum_cm - (cm[i] + cm[j]) == 100:
            dwarf[i] = 0
            dwarf[j] = 0
            break
for n in range(N):
    if dwarf[n]:
        print(cm[n])
