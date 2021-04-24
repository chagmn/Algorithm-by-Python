def solution(n):
    answer = [0 for _ in range(n + 2)]
    answer[1] = 1

    if n < 2:
        return answer[n]

    for i in range(2, n + 1):
        answer[i] = (answer[i - 1] + answer[i - 2]) % 1234567

    return answer[n]


solution(3)
solution(5)