import sys

a = int(sys.stdin.readline())
ans = [1 if a%4 == 0 and not a%100 == 0 else 1 if a%400 == 0 else 0]
print(ans[0])
