stars = int(input())

for i in range(stars):
    print("* " * (stars - stars // 2))
    print(" *" * (stars // 2))

# Q
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# input & output
# 1 -> *     3 -> * *
# 2 -> *           *
#       *         * *
#      *           *
#       *         * *
#                  *