n = int(input())

count = 0
for i in range(n):
    word = input()
    error = 0
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            new = word[j + 1 :]
            print(new)
            if new.count(word[j]) > 0:
                error += 1
    if error == 0:
        count += 1
print(count)
