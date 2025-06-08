import sys
input = sys.stdin.readline
from collections import Counter
n = int(input().rstrip())
lst = [1, 5, 10, 50]
curr = Counter()
curr[0] = 1
for _ in range (n):
    next_cnt = Counter()
    for t in curr:
        for i in lst:
            next_cnt[t + i] += curr[t]
    curr = next_cnt
print(len(curr))