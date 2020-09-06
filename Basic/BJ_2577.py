a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)

for i in range(10):
    sum = 0
    for j in range(len(result)):
        if i == int(result[j]):
            sum += 1
    print(sum)

# Q
# 세 수의 곱셈 결과의 0부터 9까지 몇 번씩 사용되렀는지 구하라

# input
# 150
# 266
# 427

# output
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0
