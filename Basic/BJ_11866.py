import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque()
arr = []
answer = []

for i in range(n):
    arr.append(i+1)

while len(arr) > 0:
    answer.append(arr[k])
    arr.remove(k)

    if k > len(arr):
        k = 
