# 내가 푼 방식
n, k = map(int, input().split())

count = 0
while True:
    if n == 1:
        break
    elif n % k != 0:
        n -= 1
        count += 1
    else:
        n = n / k
        count += 1
print(count)

# 단순하게 푸는 답 ---------
n, k = map(int, input().split())
result = 0

# n이 k 이상이면 k로 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1

# 마지막 남은 수에 대해 1식 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

# n이 엄청 큰 수일 때 빠른 해답 --------
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어 떨어지는 수) 가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

result += n - 1
print(result)