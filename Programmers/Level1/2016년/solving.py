def solution(a, b):
    month = 1
    day = 1
    index = 5  # 금요일
    dayArray = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    while True:
        if a == month and b > day - 7 and b < day + 7:
            break
        day += 7
        if (
            month == 1
            or month == 3
            or month == 5
            or month == 7
            or month == 8
            or month == 10
            or month == 12
        ):  # 31일까지
            if day > 31:
                month += 1
                day -= 31
        elif month == 2:  # 2월
            if day > 29:
                month += 1
                day -= 29
        else:
            if day > 30:
                month += 1
                day -= 30

    # 5 /
    if b > day:
        for i in range(b - day):  # 0~3
            index += 1
            if index > 6:
                index = 0
    else:
        for i in range(day - b):
            index -= 1
            if index < 0:
                index = 6

    return dayArray[index]


a = 3
b = 3

print(solution(a, b))
