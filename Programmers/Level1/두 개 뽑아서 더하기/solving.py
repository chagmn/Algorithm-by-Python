def solution(numbers):
    answer = []

    # 2중 반복문을 이용해서 모든 수를 더한다
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]

            # 중복을 방지하기 위한 if문
            if sum not in answer:
                answer.append(sum)
    answer.sort()  # 오름차순 정렬

    return answer