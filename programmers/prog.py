def solution(arr):
    answer = []
    one = 0
    two = 0
    three = 0
    for n in arr:
        if n == 1:
            one += 1
        elif n == 2:
            two += 1
        elif n == 3:
            three += 1
    max_num = max([one, two, three])
    answer.append(max_num-one)
    answer.append(max_num-two)
    answer.append(max_num-three)
    return answer


if __name__ == '__main__':
    solution([1, 2, 3])
