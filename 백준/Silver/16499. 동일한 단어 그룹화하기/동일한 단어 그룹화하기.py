import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
a = []
for i in range (n):
    a.append(Counter(sys.stdin.readline().rstrip()))

cnt = 0
vis = [False] * n
for i in range(n):
    if vis[i]: 
        continue
    vis[i] = True
    cnt += 1
    for j in range(i + 1, n):
        if a[i] == a[j]:
            vis[j] = True
print(cnt)