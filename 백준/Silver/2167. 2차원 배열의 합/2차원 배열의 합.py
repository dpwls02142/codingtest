import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
lst = []
for _ in range (n):
    lst.append(list(map(int, sys.stdin.readline().rstrip().split())))
prefix = [[0] * (m+1) for _ in range (n+1)]
for i in range (1, n+1):
    for j in range (1, m+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + lst[i-1][j-1]
# print(prefix)
k = int(sys.stdin.readline().rstrip())
for _ in range (k):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(prefix[x][y] - prefix[i-1][y] - prefix[x][j-1] + prefix[i-1][j-1])