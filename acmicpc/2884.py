import sys

h, m = map(int, sys.stdin.readline().split(' '))
H = 0
if h == 0:
    if m < 45:
        H = 24 * 60
else:
    H = h * 60

ans_m = H + m - 45
print(int(ans_m/60), int(ans_m % 60))
