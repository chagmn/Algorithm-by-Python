def solution(number, k):
    answer = ""
    start = 0
    for i in range(len(number) - k):
        max_num = number[start]
        index = start
        for j in range(start, i + k + 1):
            if max_num < number[j]:
                max_num = number[j]
                index = j
        start = index + 1
        answer += max_num
    return answer


number = "4177252841"
k = 4
solution(number, k)