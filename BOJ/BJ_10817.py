data = list(input().split(" "))

for i in range(len(data)):
    data[i] = int(data[i])

sorted_list = sorted(data, reverse=True)
print(sorted_list[1])

# Q
# 세 젇수 A, B, C가 주어질 떄,
# 두 번째로 큰 정수를 출력하는 프로그램을 작성해라

# input
# 20 30 10

# output
# 20