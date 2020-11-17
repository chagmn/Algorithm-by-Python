n = input().split("-")
arr = []

for i in n:
    sum = 0
    a = i.split("+")
    for j in a:
        sum += int(j)
    arr.append(sum)

a = arr[0]
for i in range(1, len(arr)):
    a -= arr[i]

print(a)