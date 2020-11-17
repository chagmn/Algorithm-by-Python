n = int(input())
arr = []
gap = []

for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])
    gap.append(end - start)
