import re


def solution(time, plans):
    answer = ''
    ok_plan = []  # 가능한 여행

    for plan in plans:
        if is_possible(time, plan):
            ok_plan.append(plan[0])

    answer = ok_plan[-1]  # 가능한 가장 마지막 여행지를 출력
    return answer


def time24(time_str):
    """ 00PM 형식의 스트링을 받아 24시간 형식으로 바꾸어 반환한다. """
    m = list(filter(str.isalpha, time_str))
    _h = re.findall("\d+", time_str)
    h = int(_h[0])
    if ''.join(m) == 'PM':
        hour = h + 12
    else:
        hour = h
    return hour


def is_possible(time, plan) -> bool:
    """ 가능한 여행인지 확인한다."""
    penalty = 0
    # 출발시각과 18시의 차이가 - 이면 penalty에 더한다.
    dep_penalty = time24(plan[1]) - 18
    if dep_penalty < 0:
        penalty += dep_penalty

    # 도착시각과 13시 차이가 - 이면 penalty에 더한다.
    arr_penalty = 13 - time24(plan[2])
    if arr_penalty < 0:
        penalty += arr_penalty

    if abs(penalty) < time:
        return True
    else:
        return False


if __name__ == '__main__':
    solution(3.5, [["홍콩", "11PM", "9AM"], ["엘에이", "3PM", "2PM"]])
