def HanSu(str_i, gap):
    for i in range(1, len(str_i) - 1):
        if gap != int(str_i[i + 1]) - int(str_i[i]):
            return False
        else:
            return True


n = int(input())

if n <= 99:
    print(n)
else:
    sum = 99

    for i in range(100, n + 1):
        str_i = str(i)
        gap = int(str_i[1]) - int(str_i[0])

        if HanSu(str_i, gap):
            sum += 1

    print(sum)
