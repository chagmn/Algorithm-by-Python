def solution(n, lost, reserve):
    answer = 0

    # 마지막 제한사항. 여벌소유 학생이 도난당한 경우. 두 배열에서 삭제
    _lost = [i for i in lost if i not in reserve]
    _reserve = [i for i in reserve if i not in lost]

    for i in _reserve:
        if i - 1 in _lost:
            _lost.remove(i - 1)
        elif i + 1 in _lost:
            _lost.remove(i + 1)
        # if len(_lost) == 0:
        #    break

    answer = n - len(_lost)
    return answer