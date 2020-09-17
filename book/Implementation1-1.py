# 내가 푼 방식 --------------------
n = int(input())
route = list(input().split())

start_x = 1
start_y = 1

for i in range(len(route)):
    if route[i] == "L":
        if start_y == 1:
            continue
        start_y = start_y - 1
    elif route[i] == "R":
        if start_y >= len(route):
            continue
        start_y = start_y + 1
    elif route[i] == "U":
        if start_x == 1:
            continue
        start_x = start_x - 1
    elif route[i] == "D":
        if start_x >= len(route):
            continue
        start_x = start_x + 1

print("%d %d" % (start_x, start_y))

# 답안 예시 --------------------
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)