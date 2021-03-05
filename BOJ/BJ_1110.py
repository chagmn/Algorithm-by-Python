num = int(input())
check = num
count = 0
while True:
    temp = num // 10 + num % 10
    n_num = (num % 10) * 10 + temp % 10
    count = count + 1
    num = n_num
    if n_num == check:
        break
print(count)


# Q
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
# 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙여 새로운 수가 된다.
# 이 한번이 사이클 1회이고 원래 수로 돌아올 때의 사이클 길이는?



# INPUT     OUTPUT
#  26   ->    4
#  55   ->    3
#  1    ->    60  