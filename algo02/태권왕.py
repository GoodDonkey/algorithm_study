import sys
n = int(sys.stdin.readline())
S = []
T = []
data = [list(map(int, sys.stdin.readline().rstrip().split(' '))) for _ in range(n)]
# S, T에 각각 담기
for i in range(len(data)):
    S.append(data[i][0])
    T.append(data[i][1])

print(n, data)
print(S, T)

""" 전략 1
    1) B로 안전하게 1점씩 얻기
    2) A로 지금 점수만큼 얻기 - 지금 점수가 높을 수록 유리. 
        내 점수는 S*2, 상대는 T+3 
            => S, T 작은 동안에만  A를 사용, 나머지를 B로 채우기
    -- 
    10, 20 / 11, 20 / 22, 23 / 23, 23
    --> 1점을 먼저 얻고 2배하면 더 빨리 만들 수 있음. (탐욕법 안됨.)
    전략 2
    1) 1더하고 2배? 2더하고 2배? 3더하고 2배?
        이후에 T와의 차이가 가장 적은 전략을 선택한다."""


def kick_a(s, t):
    s = s*2
    t = t+3
    return s, t


def kick_b(s, t):
    s = s+1
    return s, t


for i in range(len(S)):
    kick_a(S[i], T[i])

def greedy():
    cnt_list = []
    for i in range(len(S)):
        cnt=0
        # A 발차기
        while S[i] < T[i]:
            S[i] = S[i]*2
            T[i] = T[i]+3
            cnt += 1
        if S[i] > T[i]:  # 이떄는 S가 더 클경우.
            # while 이 끝나면 S가 더 커졌을 테니까 한단계 뒤로 돌려준다.
            S[i] = S[i]/2
            T[i] = T[i]-3
            cnt -= 1
        elif S[i] == T[i]:  # 같으면
            pass

        # B발차기
        cnt += T[i]-S[i]

        # i일 때 발차기 횟수
        cnt_list.append(cnt)
        return cnt_list






print(f"cnt_list: {greedy()}")
