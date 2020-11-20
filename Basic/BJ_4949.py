import sys

while True:
    n = sys.stdin.readline()
    arr = []
    check = 0  # yes

    if n == ".\n":
        break

    for i in range(len(n)):
        if n[i] == "(" or n[i] == "[":
            arr.append(n[i])

        elif n[i] == ")":
            if len(arr) > 0:
                if arr.pop() != "(":
                    check = 1
            elif len(arr) == 0:
                check = 1

        elif n[i] == "]":
            if len(arr) > 0:
                if arr.pop() != "[":
                    check = 1
            elif len(arr) == 0:
                check = 1

    if check == 0 and len(arr) == 0:
        print("yes")

    else:
        print("no")
