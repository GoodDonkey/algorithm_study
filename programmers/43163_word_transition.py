import re


def solution(begin: str, target: str, words: list):
    answer = 0
    history = []

    def find_match(cur_match, cnt):
        for i in range(len(begin)):
            print(cur_match, cnt)
            wish_word = cur_match.replace(cur_match[i], target[i])
            print("wish_word", wish_word)
            if wish_word in words and wish_word not in history:
                print(history)
                cur_match = wish_word
                history.append(cur_match)
                cnt += 1
                continue
            else:
                reg = cur_match.replace(cur_match[i], ".")
                print("reg", reg)
                for j in range(len(words)):
                    try:
                        if re.match(reg, words[j]) and re.match(reg, words[j]).group() not in history:
                            cur_match = re.match(reg, words[j]).group()
                            cnt += 1
                            history.append(cur_match)
                            print("re", cur_match)
                            break
                    except:
                        continue
        print("---return---")
        return cur_match, cnt

    cur_match = begin
    cnt = 0
    history.append(cur_match)

    while True:
        if target not in words:
            break
        cur_match, cnt = find_match(cur_match, cnt)
        answer = cnt
        if cur_match == target:
            break
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

