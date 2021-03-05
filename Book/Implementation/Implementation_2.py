position = input()
row = int(position[1])
column = int(ord(position[0])) - int(ord("a")) + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

case = 0
# 모든 방향에 대해 각 위치로 이동이 가능한지 확인
for i in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + i[0]
    next_column = column + i[1]
    # 해당 위치로 이동이 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        case += 1

print(case)
