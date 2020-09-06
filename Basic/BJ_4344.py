case = int(input())

for i in range(case):
    sum = 0
    avg = 0
    count = 0
    val = list(map(int, input().split()))

    for i in range(1, val[0] + 1):
        sum += val[i]

    avg = sum / val[0]

    for i in range(1, val[0] + 1):
        if val[i] > avg:
            count += 1

    print("%.3f" % ((count / val[0]) * 100.0) + "%")
