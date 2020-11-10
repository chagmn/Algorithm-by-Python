num = int(input())

arr = []
for i in range(num):
    arr.append(int(input()))

print(round(sum(arr) / num))

temp = sorted(arr, reverse=False)
print(temp[round(num / 2)])

count = [[0] * num ]
j=0
min_val = 0
for i in range(num):
    if num[i] == num[j]
        count[i] += 1

for i in range(count):
    if min_val < count[i]:
        