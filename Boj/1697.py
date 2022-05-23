# 1697. 숨바꼭질
from collections import deque

# 수빈이의 위치 N, 동생의 위치 K
n, k = map(int, input().split())

# bfs
deq = deque([n])
checked = [0] * 100001
while deq:
    now = deq.popleft()
    if now == k:
        break
    count = checked[now]

    for next_node in [now - 1, now + 1, now * 2]:
        if 0 <= next_node <= 100000:
            if not checked[next_node]:
                checked[next_node] = count + 1
                deq.append(next_node)

            if next_node == k:  # 찾음
                break

# 답
print(checked[k])
