def solution(n, lost, reserve):
    answer = n  # 전체 학생 수에서 체육복을 못 빌린 학생 수 빼기
    lost.sort()
    reserve.sort()
    for l in lost:
        if l in reserve:  # 본인의 여벌 체육복
            reserve = [i for i in reserve if i != l]
            continue
        elif l - 1 in reserve:  # 앞 번호의 여벌 체육복
            reserve = [i for i in reserve if i != l - 1]
            continue
        elif l + 1 in reserve:  # 뒷 번호의 여벌 체육복
            reserve = [i for i in reserve if i != l + 1]
            continue
        answer -= 1
    return answer