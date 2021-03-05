n, k = map(int, input().split())
money = []
count = 0

for _ in range(n):
    money.insert(0, int(input()))

for i in range(n):
    if k == 0:
        break

    count = count + (k // money[i])
    k = k % money[i]

print(count)
