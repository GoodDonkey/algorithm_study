from functools import reduce


def solution(log):
    answer = ''
    t_study = []
    # 같은 날 기록만 생각하므로 새벽 0시가 되는 경우는 생각하지 않는다.
    for s in range(0, len(log), 2):
        if get_minute(log[s+1])-get_minute(log[s]) >= 5:
            if get_minute(log[s+1])-get_minute(log[s]) > 105:
                t_study.append(105)
            else:
                t_study.append(get_minute(log[s+1])-get_minute(log[s]))
            print(t_study)
    summed = reduce(lambda a, b: a + b, t_study)
    print(summed)
    answer = f"{(summed//60):02d}:{summed%60}"
    print(answer)
    return answer


def get_minute(time: str = '') -> int:
    time_list = []
    time_list = time.split(':')
    hour_to_min = int(time_list[0])*60
    minute = int(time_list[1])
    return hour_to_min + minute



if __name__ == '__main__':
    # get_minute("08:30")
    solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"])
    solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]	)
