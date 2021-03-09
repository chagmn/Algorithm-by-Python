# 만들 수 없는 금액
import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))

coins.sort()

target = 1

for coin in coins:
    if target < coin:
        break
    target += coin

print(target)
