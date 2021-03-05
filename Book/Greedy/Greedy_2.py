n, m, k = map(int, input().split())  # n은 크기, m은 덧셈 횟수, k는 몇 번 사용 가능한지
num = list(map(int, input().split()))

num.sort()
big = num[n - 1]  # 가장 큰 수
big_next = num[n - 2]  # 두 번째로 큰 수

sum = 0

while True:
    for i in range(k):
        if m == 0:
            break
        sum += big
        m -= 1
    if m == 0:
        break
    sum += big_next
    m -= 1

print(sum)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 반복되는 수열을 이용한 풀이

count = int(m / (k + 1)) * k
count += m % (k + 1)

sum = 0
sum += (count) * big  # 첫 번째 큰 수 더하기
sum += (m - count) * big_next  # 두 번째 큰 수 더하기

print(sum)