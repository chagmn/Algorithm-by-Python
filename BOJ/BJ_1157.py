word = input().upper()

count = []

for i in set(word):
    count.append(word.count(i))

idx = [i for i, x in enumerate(count) if x == max(count)]

if len(idx) > 1:
    print("?")
else:
    print(list(set(word))[count.index(max(count))])
