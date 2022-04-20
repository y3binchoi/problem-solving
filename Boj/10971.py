import sys
from itertools import permutations


def cal_cost(i, cost):
    global min_cost
    if i == N - 1:
        if W[rt[N - 1]][rt[0]]:  # 첫 노드로 되돌아가는 경로 존재
            cost += W[rt[N - 1]][rt[0]]
            min_cost = min(min_cost, cost)
        else:
            return
    else:
        if W[rt[i]][rt[i + 1]]:  # 비용!=0 즉 경로가 존재 하면
            cal_cost(i + 1, cost + W[rt[i]][rt[i + 1]])
        else:
            return


N = int(sys.stdin.readline())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
node = [i for i in range(N)]  # 0 ~ N-1
routes = list(permutations(node, N))
min_cost = 1000000 * 10
for rt in routes:  # rt=루트 튜플
    if rt[0] != node[0]:
        break
    cal_cost(0, 0)
print(min_cost)