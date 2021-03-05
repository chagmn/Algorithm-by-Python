import sys


def binary_search(target, start, end, arr_n):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == arr_n[mid]:
        return 1
    elif target < arr_n[mid]:
        return binary_search(target, start, mid - 1, arr_n)
    else:
        return binary_search(target, mid + 1, end, arr_n)


n = int(sys.stdin.readline())
arr_n = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

for i in arr_m:
    start = 0
    end = len(arr_m) - 1
    print(binary_search(i, start, end, arr_n))
