import sys
input = sys.stdin.readline
from itertools import combinations
hat = []
for _ in range (9):
    hat.append(int(input()))

for i in combinations(hat, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break