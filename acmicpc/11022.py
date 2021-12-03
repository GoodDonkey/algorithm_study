import sys

T = sys.stdin.readline()
digits = []
for i in range(int(T)):
    digits.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    print(f"Case #{i+1}: {digits[i][0]} + {digits[i][1]} = {sum(digits[i])}")
