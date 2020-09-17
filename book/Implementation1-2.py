n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)

# 만약 '3시 30분 25초' 라고 하면 이를 033025 라는 문자열로 바꾸고
# 이 안에 '3' 이라는 문자가 포함되었는지 확인하면 되는 문제다.