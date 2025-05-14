import sys
input = sys.stdin.readline
from collections import Counter

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))

a_cnt = Counter(a)
res = [-1] * n
stack = []
for i in range (n-1, -1, -1):
    while stack and a_cnt[a[i]] >= a_cnt[stack[-1]]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    stack.append(a[i])
print(' '.join(map(str, res)))