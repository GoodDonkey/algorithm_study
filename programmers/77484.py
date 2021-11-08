def solution(lottos: list, win_nums: list):
    answer = []
    n_li = []
    chance = 0
    for n in lottos:
        if n == 0:
            chance += 1  # 0의 개수
        elif n in win_nums:
            n_li.append(n)  # 맞춘 번호
    best_index = len(n_li) + chance -1
    if len(n_li) == 0:
        worst_index = 0
    else:
        worst_index = len(n_li) -1
    rank = [6, 5, 4, 3, 2, 1]
    answer.append(rank[best_index])
    answer.append(rank[worst_index])
    return answer


if __name__ == '__main__':
    solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
