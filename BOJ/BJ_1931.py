n = int(input())
arr = []
count = 0

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

start = 0

for i in arr:
    if i[0] >= start:
        start = i[1]
        count += 1

print(count)