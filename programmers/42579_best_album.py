

def solution(genres, plays):
    answer = []
    dic = {}
    song_dic = {}

    zipper = list(zip(genres, plays))
    print(zipper)

    for item in zipper:
        if item[0] in dic:
            dic[item[0]] += item[1]
        else:
            dic[item[0]] = item[1]
    print("dic", dic)

    for i in range(len(zipper)):
        song_dic[i] = zipper[i]
    print(song_dic)

    # 장르 순위 내림차순
    genre_rank = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    song_rank = sorted(song_dic.items(), key=lambda x: x[1][1], reverse=True)
    print(genre_rank)
    print(song_rank)

    # 장르 순 -> 플레이 횟수
    for genre in genre_rank.keys():
        cnt = 0
        for i, song in song_rank:
            if song[0] == genre:
                cnt += 1
                answer.append(i)
                if cnt == 2:
                    break
    return answer



print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
