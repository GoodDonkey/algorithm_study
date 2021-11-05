import sys

T = int(sys.stdin.readline())

A_list, B_list = [], []

for _ in range(T):
    A, B = tuple(map(int, sys.stdin.readline().split(' ')))
    A_list.append(A)
    B_list.append(B)

for i in range(T):
    print(A_list[i]+B_list[i])