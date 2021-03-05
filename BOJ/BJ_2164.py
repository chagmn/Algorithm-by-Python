import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    queue.append(i + 1)

i = 1
while len(queue) > 1:
    if i % 2 == 1:
        queue.popleft()
    elif i % 2 == 0:
        a = queue.popleft()
        queue.append(a)
    i += 1

print(queue.popleft())