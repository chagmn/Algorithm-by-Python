# 기능개발
import math


def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    count = 1

    for i in range(len(progresses) - 1):
        if days[i] < days[i + 1]:
            answer.append(count)
            count = 1
        else:
            days[i + 1] = days[i]
            count += 1

    answer.append(count)

    return answer