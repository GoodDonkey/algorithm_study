import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

if a > 0:
    if b > 0:
        ans = 1
    else:
        ans = 4
else:
    if b > 0:
        ans = 2
    else:
        ans = 3

print(ans)