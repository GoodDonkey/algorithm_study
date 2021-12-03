import sys

N = "%02d" % (int(sys.stdin.readline()))
M = N
i = 0

while True:
    i += 1
    s = sum(map(int, N))
    ss = str(s)[-1]
    N = N[1]+ss
    if N == M:
        print(i)
        break

