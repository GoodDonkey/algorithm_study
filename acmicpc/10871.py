import sys

N, X = map(int, sys.stdin.readline().rstrip().split(" "))

A = list(map(int, sys.stdin.readline().rstrip().split(" ")))

for n in A:
    if n < X:
        print(n, end=" ")
