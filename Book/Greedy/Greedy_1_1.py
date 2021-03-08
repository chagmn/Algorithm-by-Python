# 모험가 길드
import sys

n = int(sys.stdin.readline())  # 모험가 수
x = list(map(int, sys.stdin.readline().split()))  # 공포도 값
group = 0  # 그룹 수
count = 0  # 그룹에 있는 인원

for i in x:  # 공포도 하나 꺼내서
    count += 1  # 인원 1증가
    if count >= i:  # 인원이 공포도보다 크거나 같으면
        group += 1  # 그룹 1증가(다음 그룹)
        count = 0  # 인원은 0 초기화

print(group)