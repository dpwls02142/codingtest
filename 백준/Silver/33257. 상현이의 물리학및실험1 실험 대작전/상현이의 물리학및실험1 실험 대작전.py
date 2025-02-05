import sys

n, e = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
a.sort()

cnt = 1

for i in range(1, n):
    if a[i] - a[i-1] >= e:
        cnt += 1

print(cnt)