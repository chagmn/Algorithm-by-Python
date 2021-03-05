from collections import deque

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 들린 곳은 큐에 저장

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 넘어가지 않도록
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 0인 곳에 가지 않도록
            if array[nx][ny] == 0:
                continue

            # 들린 곳에 가면 거리를 기록
            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx, ny))

    return array[n - 1][m - 1]


print(bfs(0, 0))
