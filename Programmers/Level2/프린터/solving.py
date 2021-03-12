from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque(
        (val, index) for index, val in enumerate(priorities)
    )  # 순서를 먼저 -> 우선순위 최댓값을 위해서

    while len(dq) > 0:
        data = dq.popleft()

        # 우선순위가 가장 큰 값보다 작을 때 -> 아직 프린트 못함
        if data[0] < max(dq)[0]:
            dq.append(data)

        # 우선순위가 작거나 같을 때 -> answer 값 증가
        else:
            answer += 1
            # 만약 사용자가 요청한 문서라면 반복문 탈출
            if data[1] == location:
                break

    return answer