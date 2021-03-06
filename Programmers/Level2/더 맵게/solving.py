import heapq


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < k:
        if len(scoville) > 1:
            heapq.heappush(
                scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            )
            answer += 1
        else:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
