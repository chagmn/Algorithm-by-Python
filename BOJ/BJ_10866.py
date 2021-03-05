from collections import deque
import sys

queue = deque()
num = int(sys.stdin.readline())

for i in range(num):
    n = sys.stdin.readline().split()

    if n[0] == "push_front":
        queue.appendleft(n[1])
    elif n[0] == "push_back":
        queue.append(n[1])
    elif n[0] == "pop_front":
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print("-1")
    elif n[0] == "pop_back":
        if len(queue) > 0:
            print(queue.pop())
        else:
            print("-1")
    elif n[0] == "size":
        print(len(queue))
    elif n[0] == "empty":
        if len(queue) > 0:
            print("0")
        else:
            print("1")
    elif n[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print("-1")
    elif n[0] == "back":
        if len(queue) > 0:
            print(queue[len(queue) - 1])
        else:
            print("-1")