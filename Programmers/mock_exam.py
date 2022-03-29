def solution(answers):
    highest_score = []
    gave_up = [[1, 2, 3, 4, 5],  # 수포자1의 답안지
               [2, 1, 2, 3, 2, 4, 2, 5],  # 수포자2의 답안지
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]  # 수포자3의 답안지
    score = [0] * 3  # 수포자들의 점수
    temp = [0] * 3
    for ans in answers:
        for i in range(3):
            if ans == gave_up[i][temp[i]]:
                score[i] += 1
            temp[i] += 1
            if temp[i] >= len(gave_up[i]):
                temp[i] -= len(gave_up[i])
    max_score = max(score)
    for s in range(3):
        if score[s] >= max_score:
            highest_score.append(s + 1)
    return highest_score
