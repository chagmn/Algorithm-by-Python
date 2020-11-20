import sys

k = int(sys.stdin.readline())
arr = []
sum = 0

for _ in range(k):
    n = int(sys.stdin.readline())

    if n == 0:
        arr.pop()
    else:
        arr.append(n)

for i in arr:
    sum += i

print(sum)