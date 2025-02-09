import sys

t = int(sys.stdin.readline().rstrip())

for _ in range (t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    res = [[0] * (n+1) for _ in range(k+1)]

    for i in range (1, n+1):
        res[0][i] = i

    for i in range (1, len(res)):
        for j in range (1, len(res[i])):
            res[i][j] = res[i-1][j] + res[i][j-1]

    print(res[k][n])