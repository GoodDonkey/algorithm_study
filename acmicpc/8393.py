import sys
from functools import reduce


def solution():
    n = int(sys.stdin.readline())
    li = [*range(n+1)]
    suming = reduce(lambda a, b: a + b, li, 0)
    print(suming)


if __name__ == '__main__':
    solution()
