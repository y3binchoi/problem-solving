def makePers():
    for n in range(N):
        if used[n]:
            continue
        else:
            used[n] = 1
            temp.append(n + 1)
            makePers()
            if 0 not in used:  # 모든 숫자 사용
                pers.append(list(temp))
        used[n] = 0
        temp.pop()


N = int(input())
used = [0 for _ in range(N)]  # 숫자 사용 여부
pers = []  # 모든 순열
temp = []  # 순열 임시 저장
makePers()
for p in pers:
    print(*p, end=' ')
    print()