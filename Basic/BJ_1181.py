n = int(input())

arr = []

for _ in range(n):
    word = str(input())
    word_len = len(word)
    arr.append((word, word_len))

arr = list(set(arr))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0])