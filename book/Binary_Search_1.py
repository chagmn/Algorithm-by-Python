def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid

        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())  # 가계부품
n_arr = list(map(int, input().split()))
n_arr.sort()

m = int(input())  # 찾는 부품
m_arr = list(map(int, input().split()))

for i in m_arr:
    result = binary_search(n_arr, i, 0, n - 1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
