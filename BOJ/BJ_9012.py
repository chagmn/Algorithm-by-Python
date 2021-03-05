import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline())


for i in arr:
    correct = 1
    check = []
    for j in range(len(i)):
        if i[j] == "(":
            check.append(i[j])
        elif i[j] == ")":
            if len(check) == 0:
                correct = 0
            else:
                check.pop()

    if correct == 0 or len(check) > 0:
        print("NO")
    else:
        print("YES")