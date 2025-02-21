import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
b = []
cnt = 0
for _ in range (n):
    a = list(map(int, sys.stdin.readline().rstrip()))
    b.append(a)

for l in range(min(n, m)):
    for i in range(n - l):
        for j in range(m - l):
            if (b[i][j] == b[i+l][j] == b[i][j+l] == b[i+l][j+l]):
                cnt = max(cnt, (l+1) * (l+1))

print(cnt)