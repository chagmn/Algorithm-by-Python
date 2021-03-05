n, m = map(int, input().split())

number = [i + 1 for i in range(n)]
check = [False] * n
arr = []


def dfs(count):
    if count == m:
        print(*arr)
        return

    for i in range(n):
        if check[i]:
            continue

        check[i] = True
        arr.append(number[i])

        dfs(count + 1)
        arr.pop()
        check[i] = False


dfs(0)