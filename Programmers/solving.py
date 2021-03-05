import sys


def binary_search(cards, target):
    start = 0
    end = len(cards) - 1
    count = 0

    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            count += 1
            cards.pop(mid)
            start = 0
            end = len(cards) - 1
        elif target < cards[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return count


n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
count_num = list(map(int, sys.stdin.readline().split()))

for i in count_num:
    print(binary_search(cards, i), end=" ")
