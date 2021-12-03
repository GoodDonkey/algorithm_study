import sys

T = sys.stdin.readline()
digits = []
for i in range(int(T)):
    digits.append(map(int, sys.stdin.readline().rstrip().split(" ")))
    print(f"Case #{i+1}: {sum(digits[i])}")
