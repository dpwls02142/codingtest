import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

d = deque()
res = []

for i in range (n):
    while d and d[0] < i - l + 1:
        d.popleft()
    while d and a[d[-1]] > a[i]:
        d.pop()
    d.append(i)
    res.append(a[d[0]])
print(' '.join(map(str, res)))