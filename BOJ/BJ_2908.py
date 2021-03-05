n, m = map(str, input().split())

new_n = ""
new_m = ""

for i in range(len(n)):
    new_n += n[len(n) - 1 - i]

for i in range(len(m)):
    new_m += m[len(m) - 1 - i]

if new_n > new_m:
    print(new_n)
else:
    print(new_m)