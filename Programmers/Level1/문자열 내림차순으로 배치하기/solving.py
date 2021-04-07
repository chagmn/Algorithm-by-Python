def solution(s):
    answer = sorted(s, reverse=True)
    return "".join(answer)


s = "Zbcdefg"
print(solution(s))