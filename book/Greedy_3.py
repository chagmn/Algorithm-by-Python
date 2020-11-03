# 내가 푼 방식
n, m = map(int, input().split())

for i in range(n):
    num = list(map(int, input().split()))
    num.sort()
    min_num = num[0]
    if min_num > num[0]:
        min_num = num[0]

print(min_num)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 책 풀이 - min() 함수 사용

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 책 풀이 - 2중 반복문 구조

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)