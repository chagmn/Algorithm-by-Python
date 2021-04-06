def solution(number, k):
    stack = []
    for i in number:
        while stack and i > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)

    if k > 0:
        for i in range(k):
            stack.pop()

    print("".join(stack))


number = "1231234"
k = 3
solution(number, k)
