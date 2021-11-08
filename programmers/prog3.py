def solution(ings, menu, sell):
    answer = 0
    ings_list = [a.split(" ") for a in ings]
    ings_dict = {}
    for k, v in ings_list:
        ings_dict[k] = v
    print(ings_dict)

    # 메뉴, 판매가-생산비 dict를 만들어야 한다.
    margin_dict = {}
    for item in menu:
        l_item = item.split(" ")
        prod_price = 0  # 생산가 초기화
        for s in l_item[1]:  # arraak ...
            prod_price += int(ings_dict[s])
        margin = int(l_item[2])-prod_price
        margin_dict[l_item[0]] = margin  # 매뉴별 생산가

    for n in sell:
        n_list = n.split(" ")
        answer += margin_dict[n_list[0]]*int(n_list[1])
    print(answer)
    return answer


if __name__ == '__main__':
    solution(["r 10", "a 23", "t 124", "k 9"],
             ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
              "JUICE rra 55", "WATER a 20"],
             ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"])
