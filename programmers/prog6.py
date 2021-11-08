def solution(grid, clockwise):
    answer = []
    # 1 / 21 / 221 / 2221 / ...
    # clockwise 에 따라 뽑는 방향을 다르게 한다.
    # grid[-1] 부터 조회 -> [-1]부터냐 [1] 부터냐.
    if clockwise == 'true':
        for i in range(len(grid)):
            temp = []
            # i보다 작은 건 2개씩 뽑는다.
            if not i == 0:
                for j in range(i):  # -1 / -1, -2 / -1, -2, -3 ...
                    # 21 / 43 / 65 ...
                    # -3-4 / -1-2
                    temp.append(grid[-j-1][i-len(grid[i]):i-len(grid[i]):-1])
            # i번째는 1개만 뽑고
            temp.append(grid[-i-1][0])

            temp_str = ''.join(temp)
            answer.append(temp_str)
            print(answer)
    else:
        pass
    return answer


if __name__ == '__main__':
    d = "56789"
    # print(d[-2])
    solution(["1", "234", "56789"], 'true')
    # solution(["A", "MAN", "DRINK", "WATER11"], 'false')
