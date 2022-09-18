from collections import deque


def solution(begin, target, words):
    # target이 words 안에 없으면 변환 불가
    if target not in words:
        return 0
    # words가 50개로 길지 않기 때문에 따로 연결 그래프를 생성하지 않음
    # 큐에 단어와 단어의 인덱스를 함께 넣음
    # visited에 단계를 저장하여 방문처리
    # words를 인덱스로 조회하여 방문하지 않은 단어 중 변환 가능한 다음 단계를 물색
    words.append(begin)
    dq = deque()
    dq.append((begin, len(words) - 1))
    visited = [0] * len(words)
    visited[-1] = 1
    while dq:
        word, i = dq.popleft()
        for j in range(len(words)):
            if i == j:
                continue
            if visited[j] > 0:
                continue
            if not word_diff1(words[i], words[j]):
                continue
            dq.append((words[j], j))
            visited[j] = visited[i] + 1
            if words[j] == target:
                # begin부터 1로 카운트 했으므로 -1단계의 과정을 거친 것
                return visited[j] - 1


# input : 두 개의 단어
# output: 두 단어가 알파벳 한 개만 차이나는지
def word_diff1(w1, w2):
    length = len(w1)
    count = 0
    for i in range(length):
        if w1[i] != w2[i]:
            count += 1
    return True if count == 1 else False
