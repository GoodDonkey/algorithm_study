import sys

A, B = 1, 1

while not A == 0 and not B == 0:
    A, B = map(int, sys.stdin.readline().rstrip().split(" "))
    if not A == 0 and not B == 0:
        print(A + B)
