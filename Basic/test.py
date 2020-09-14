n = int(input())

for i in range(n):
    val = list(input().split())
    str_val = val[1]
    for j in range(len(str_val)):
        for k in range(int(val[0])):
            print(str_val[j], end="")
    print()
    val.clear()
