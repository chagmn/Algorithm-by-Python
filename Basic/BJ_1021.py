from collections import deque

n, m = map(int, input().split(" "))
answer = list(map(int, input().split(" ")))
deque = deque()

for i in range(n):
    deque.append(i + 1)

count = 0

while len(answer) > 0:
    if answer[0] == deque[0]:
        answer.remove(answer[0])
        deque.popleft()

    elif deque.index(answer[0]) <= (len(deque) // 2):
        deque.append(deque[0])
        deque.popleft()
        count += 1

    elif deque.index(answer[0]) > (len(deque) // 2):
        deque.insert(0, deque[len(deque) - 1])
        deque.pop()
        count += 1

print(count)