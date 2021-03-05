n, m = map(int, input().split())
arr = []


def backtracking(depth, n, m):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(depth, n):
        arr.append(i + 1)
        backtracking(depth + 1, n, m)
        arr.pop()
        print(i, arr)


backtracking(0, n, m)
