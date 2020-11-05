n = input()

sum = len(n)

for i in range(len(n)):
    if n[i].upper() >= "A" and n[i].upper() <= "C":
        sum += 2
    elif n[i].upper() >= "D" and n[i].upper() <= "F":
        sum += 3
    elif n[i].upper() >= "G" and n[i].upper() <= "I":
        sum += 4
    elif n[i].upper() >= "J" and n[i].upper() <= "L":
        sum += 5
    elif n[i].upper() >= "M" and n[i].upper() <= "O":
        sum += 6
    elif n[i].upper() >= "P" and n[i].upper() <= "S":
        sum += 7
    elif n[i].upper() >= "T" and n[i].upper() <= "V":
        sum += 8
    elif n[i].upper() >= "W" and n[i].upper() <= "Z":
        sum += 9

print(sum)
