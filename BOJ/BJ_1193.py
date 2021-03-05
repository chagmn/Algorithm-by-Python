input_num = int(input())

line = 0
max_num = 0

while input_num > max_num:
    line += 1
    max_num += line

gap = max_num - input_num
if line % 2 == 0:
    top = line - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = line - gap
print(f"{top}/{bottom}")
