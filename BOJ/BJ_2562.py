import sys

maxValue = 0
maxValueIndex = 1

for i in range(1, 10):
    value = int(sys.stdin.readline())
    if maxValue < value:
        maxValue = value
        maxValueIndex = i

print(maxValue)
print(maxValueIndex)
