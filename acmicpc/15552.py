import sys

T = int(sys.stdin.readline())
li = []
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split(' '))
    li.append(A+B)

for i in range(T):
    print(li[i])
