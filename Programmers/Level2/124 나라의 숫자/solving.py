def solution(n):
    answer = ""
    namuji = ["4", "1", "2"]

    while n:
        answer = namuji[n % 3] + answer

        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n = n // 3
    return answer