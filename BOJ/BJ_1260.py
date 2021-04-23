# DFS와 BFS
import sys


def dfs(array, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and array[v][i] == 1:
            dfs(array, i, visited)


def bfs(v):
    queue = [v]
    visited[v] = True

    while queue:
        start = queue.pop(0)
        print(start, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and array[start][i] == 1:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, sys.stdin.readline().split(" "))
array = [[0] * (n + 1) for i in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    start, end = list(map(int, sys.stdin.readline().split()))
    array[start][end] = 1
    array[end][start] = 1


dfs(array, v, visited)
print()
visited = [False] * (n + 1)
bfs(v)