from collections import deque

num = int(input())

for i in range(num):
    # n = 문서 수, m = 몇번째로 인쇄되는지 궁금한 문서 인덱스
    n, m = map(int, input().split())
    # 중요도 입력받기
    queue = deque(map(int, input().split()))
    target = [0] * len(queue)
    target[m] = 1
    count = 0

    if n == 1:
        print("1")
    else:
        while queue:
            if queue[0] < max(queue):
                queue.append(queue[0])
                queue.popleft()
                target.append(target.pop(0))
            elif queue[0] == max(queue):
                val = queue.popleft()
                count += 1
                if target.pop(0) == 1:
                    break
        print(count)
