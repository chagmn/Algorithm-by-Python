n = int(input())


def backtracking(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                continue


backtracking(n)