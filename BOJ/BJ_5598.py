n = input()
answer = ""

for i in range(len(n)):
    if (ord(n[i]) - 3) >= 65:
        answer += chr(ord(n[i]) - 3)
    else:
        answer += chr(ord(n[i]) + 23)


print(answer)
