n, m, c = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 -> 자기 자신 => 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(m):
    max = graph[c][0]

    if max < graph[c][i]:
        max = graph[c][i]

print()
