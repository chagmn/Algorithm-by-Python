# DFS와 BFS
import sys


def dfs(array, start, visited):
    visited[start] = True
    print(start, end=" ")
    for i in array[start]:
        if not visited[i]:
            dfs(array, i, visited)


n, m, v = map(int, sys.stdin.readline().split(" "))
array = []
visited = [False] * (n + 1)

for i in range(m):
    start, end = list(map(int, sys.stdin.readline().split()))
    array.append([start, end])

dfs(array, v, visited)
