def solution(array, commands):
    answer = []

    # commands 값을 하나씩 할당
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        arr = array[i - 1 : j]  # i~j 사이 값만 자르기
        arr.sort()  # 오름차순 정렬
        answer.append(arr[k - 1])
    return answer
