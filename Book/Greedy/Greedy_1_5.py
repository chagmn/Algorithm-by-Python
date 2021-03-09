# 볼링공 고르기

import sys

n, m = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

array = [0] * 11  # 1~10 담을 배열 -> 공의 무게

for i in weights:
    array[i] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i]  # 현재 무게보다 작은 무게는 제외 -> a가 선택 가능함
    result += array[i] * n  # b가 선택 가능한 것과 곱하기

print(result)