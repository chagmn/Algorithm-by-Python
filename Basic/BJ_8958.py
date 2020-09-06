n = int(input())


for i in range(n):
    sum_val = 0
    point = 0
    val = input()

    for j in range(len(val)):
        if val[j] == "O":
            point += 1
            sum_val += point
        else:
            point = 0

    print(sum_val)

# Q
# O는 문제를 맞고 X는 문제를 틀림.
# 문제를 맞는 경우 그 문제의 점수는 그 문제까지의 연속된 맞은 개수.
# OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점

# input            ->      output
# 5
# OOXXOXXOOO                 10
# OOXXOOXXOO                  9
# OXOXOXOXOXOXOX              7
# OOOOOOOOOO                 55
# OOOOXOOOOXOOOOX            30