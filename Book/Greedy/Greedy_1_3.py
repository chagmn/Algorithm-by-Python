# 문자열 뒤집기
import sys

s = sys.stdin.readline()
zero_count = 0  # 전체를 0으로 바꾸는 경우
one_count = 0  # 전체를 1로 바꾸는 경우

if s[0] == "0":
    one_count += 1
else:
    zero_count += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:  # 현재 수가 다음 수랑 다를 경우
        if s[i + 1] == "1":  # 다음 수가 1이면
            zero_count += 1
        elif s[i + 1] == "0":  # 다음 수가 0이면
            one_count += 1

# 두 경우 중 최솟값 출력
print(min(zero_count, one_count))
