import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
m = int(input().rstrip())
c = list(map(int, input().rstrip().split()))
res = deque()
for i in range (n):
    if a[i] == 0:
        res.appendleft(b[i])
for i in range (m):
    res.append(c[i])
    print(res.popleft(), end=' ')