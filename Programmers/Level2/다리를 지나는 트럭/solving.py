from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)  # 대기 중인 트럭
    on_bridge = deque([0] * bridge_length)  # 건너는 트럭
    total_weights = 0  # 도로 위 트럭 무게

    while on_bridge:  # 다리에 트럭이 없을 때까지 진행
        answer += 1
        total_weights -= on_bridge.popleft()

        if truck_weights:  # 대기 중인 트럭이 있으면
            if total_weights + truck_weights[0] <= weight:  # 견디는 무게보다 작다면
                going_truck = truck_weights.popleft()
                on_bridge.append(going_truck)  # 트럭 출발
                total_weights += going_truck  # 도로 위 트럭 무게 증가

            else:  # 견디는 무게보다 크면 다리를 통과 못하니 0 추가
                on_bridge.append(0)

    return answer