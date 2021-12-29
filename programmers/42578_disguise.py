from functools import reduce
from collections import Counter

def solution(clothes):
    hashmap = dict()
    for item in clothes:
        try:
            if hashmap[item[1]]:
                hashmap[item[1]].append(item[0])
        except:
            hashmap[item[1]] = [item[0]]

    answer = reduce(lambda x, y: x*y, [len(v) + 1 for v in hashmap.values()]) - 1

    return answer


def solution2(clothes):
    cnt = Counter([cloth_key for cloth_value, cloth_key in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x * y, [v + 1 for v in cnt.values()]) - 1
    return answer


print(solution2([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
