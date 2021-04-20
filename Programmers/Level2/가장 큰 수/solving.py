def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    print(numbers)
    return str(int("".join(numbers)))


print(solution([0, 0, 0]))
