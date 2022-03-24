def solution(n, lost, reserve):
    answer = n  # 전체 학생 수에서 체육복을 못 빌린 학생 수 빼기
    ex_lost = [i for i in lost if i not in reserve]  # 여벌 있는 사람은 자기꺼 입어라
    ex_reserve = [i for i in reserve if i not in lost]
    ex_lost.sort()
    ex_reserve.sort()

    for l in ex_lost:
        if l - 1 in ex_reserve:  # 앞 번호의 여벌 체육복
            ex_reserve = [i for i in ex_reserve if i != l - 1]
            continue
        elif l + 1 in ex_reserve:  # 뒷 번호의 여벌 체육복
            ex_reserve = [i for i in ex_reserve if i != l + 1]
            continue
        answer -= 1
    return answer
