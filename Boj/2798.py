import sys

input = sys.stdin.readline
N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)  # 큰 수부터 선택
blackjack = 0  # 답
total = 0  # 선택한 3개의 카드의 합
for i in range(N - 2):
    total = 0
    total += cards[i]
    for j in range(i + 1, N - 1):
        total += cards[j]
        if total > M:  # 두 번째 수를 더해서 이미 M을 넘으면 더 더해볼 필요 없음
            total -= cards[j]
            break
        for k in range(j + 1, N):
            total += cards[k]
            if M >= total > blackjack:  # 이미 최대 합을 찾았 다면 더 작은 카드는 선택 해보지 않아도 됨
                blackjack = total
                total -= cards[k]
                break
            total -= cards[k]
        total -= cards[j]
print(blackjack)
