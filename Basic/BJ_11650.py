import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()

for i in range(n):
    print(arr[i][0], end=" ")
    print(arr[i][1])
