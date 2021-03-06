def solution(s):
    answer = ""
    numbers = s.split(" ")
    min = int(numbers[0])
    max = int(numbers[0])

    for i in range(len(numbers)):
        if max < int(numbers[i]):
            max = int(numbers[i])
        if min > int(numbers[i]):
            min = int(numbers[i])

    answer = str(min) + " " + str(max)

    return answer