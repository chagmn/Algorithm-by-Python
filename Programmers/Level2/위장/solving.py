def solution(clothes):
    answer = 1
    dic = dict()

    for name, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    for i in dic.values():
        answer *= i + 1

    return answer - 1


clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]
print(solution(clothes))