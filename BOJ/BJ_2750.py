import sys
from collections import Counter


def one(arr):
    print("%.f" % (sum(arr) / num))


def two(arr):
    arr.sort()
    print(arr[num // 2])


def three(arr):
    k = Counter(arr).most_common()
    if len(arr) > 1:
        if k[0][1] == k[1][1]:
            print(k[1][0])
        else:
            print(k[0][0])
    else:
        print(arr[0])


def four(arr):
    print(arr[num - 1] - arr[0])


num = int(sys.stdin.readline())

arr = []
for _ in range(num):
    arr.append(int(sys.stdin.readline()))

one(arr)
two(arr)
three(arr)
four(arr)