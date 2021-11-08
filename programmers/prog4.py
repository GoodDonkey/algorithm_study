def solution(s):
    answer = []

    # 다르면 연속하는 문자의 개수를 차례로 센다.
    cnt = 0
    for i, char in enumerate(s):
        print(char)
        if i < len(s)-1:
            if char == s[i+1]:
                cnt += 1
            else:
                answer.append(cnt + 1)  # a -> b로 바뀔때도 개수를 세기 때문에 + 1
                cnt = 0
        else:
            answer.append(cnt + 1)

    # 처음과 끝이 같으면 양쪽의 개수 더함
    if s[0] == s[-1]:
        answer[0] += answer[-1]
        answer.pop()

    print(sorted(answer))
    return sorted(answer)


if __name__ == '__main__':
    solution("aaabbaaa")
    solution("wowwow")