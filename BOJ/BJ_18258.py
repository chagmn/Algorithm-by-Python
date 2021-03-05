from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    k = sys.stdin.readline().split()

    if k[0] == "push":
        queue.append(k[1])
    elif k[0] == "pop":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif k[0] == "size":
        print(len(queue))
    elif k[0] == "empty":
        if len(queue) == 0:
            print("1")
        else:
            print("0")
    elif k[0] == "front":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[0])

    elif k[0] == "back":
        if len(queue) == 0:
            print("-1")
        else:
            print(queue[len(queue) - 1])
