n, m = map(int, input().split())
arr = []


def backtracking(depth, n, m):
    if depth == m:
        print(" ".join(map(str, arr)))
        return

    for i in range(n):
        arr.append(i + 1)
        backtracking(depth + 1, n, m)
        arr.pop()


backtracking(0, n, m)
