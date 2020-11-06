finish = int(input())

start = 1
plus = 6
room = 1

if finish == 1:
    print("1")
else:
    while True:
        start += plus
        room += 1
        if finish <= start:
            print(room)
            break
        plus += 6
