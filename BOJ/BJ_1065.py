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

"""
< 한수 문제 >
어떤 양의 정수 x의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.

1보다 크고 x보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성.

< 입력 -> 출력 >
110 -> 99
1 -> 1
210 -> 105
1000 -> 144
"""
