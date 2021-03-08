# 곱하기 혹은 더하기
import sys

s = sys.stdin.readline()
max_sum = int(s[0])  # 최댓값을 첫 값으로 초기화

for i in range(1, len(s) - 1):
    # 첫 값이 0인 경우도 더하기, 0과 1은 더하기
    if int(s[i]) <= 1 or max_sum == 0:
        max_sum += int(s[i])
    else:  # 그 외의 수는 곱하기
        max_sum *= int(s[i])

print(max_sum)