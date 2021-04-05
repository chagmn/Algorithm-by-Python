def solution(prices):
    answer = []

    for i in range(len(prices)):
        if i == len(prices) - 1:
            answer.append(0)
            break
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    return answer


prices = [1, 2, 3, 2, 3]

solution(prices)