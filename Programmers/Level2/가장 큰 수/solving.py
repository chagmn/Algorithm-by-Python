def solution(numbers):
    answer = ""
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str("".join(numbers))


print(solution([0, 0, 0]))
