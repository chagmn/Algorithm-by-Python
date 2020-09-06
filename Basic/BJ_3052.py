remain = []
sum = 0

for i in range(10):
    val = int(input())
    temp = val % 42
    if temp not in remain:
        remain.append(temp)
        sum += 1

print(sum)

# Q
# 10개수를 입력 받고 42로 나눈 나머지를 구하는데 서로 다른 값의 나머지가 몇개인지 출력해라

# input
# 39
# 40
# 41
# 42
# 43
# 44
# 82
# 83
# 84
# 85

# output
# 6