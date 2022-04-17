import sys


def counselProfit(_day, _profit):
    global max_profit
    if _day > N:  # 이미 퇴사날을 넘겼으면 선택 못함
        return
    max_profit = max(max_profit, _profit)
    if _day == N:  # 퇴사 전 마지막 날
        return
    # 현재 날짜 선택
    counselProfit(_day + time_price[_day][0], _profit + time_price[_day][1])
    # 현재 날짜 선택 X
    counselProfit(_day + 1, _profit)


N = int(sys.stdin.readline())
time_price = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_profit = 0
counselProfit(0, 0)
print(max_profit)
