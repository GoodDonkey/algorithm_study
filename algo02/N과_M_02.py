import sys
from itertools import combinations


def main():
    n, m = tuple(map(int, sys.stdin.readline().rstrip().split(' ')))

    comb_list = list(combinations(range(1, n+1), m))

    for comb in comb_list:
        for j in range(m):
            sys.stdout.write(str(comb[j])+" ")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()