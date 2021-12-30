from itertools import combinations


def solution(numbers: list, target: int):
    answer = 0
    leaves = [0]
    for cur_num in numbers:
        temp = []
        for cur_sum in leaves:
            temp.append(cur_sum + cur_num)
            temp.append(cur_sum - cur_num)
        leaves = temp

    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer

print(solution([1, 1, 1, 1, 1], 3))
