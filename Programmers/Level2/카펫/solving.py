def solution(brown, yellow):
    array = [
        (yellow // i, i) for i in range(1, int(yellow ** 0.5) + 1) if yellow % i == 0
    ]
    for m, n in array:
        if (m + 2) * (n + 2) == brown + yellow:
            return [m + 2, n + 2]


brown = 16
yellow = 5
print(solution(brown, yellow))