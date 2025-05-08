import sys
input = sys.stdin.readline
n = int(input().rstrip())
res = [[0 for _ in range (101)] for _ in range (101)]
for _ in range (n):
    a, b = map(int, input().rstrip().split())
    for i in range (a, 10 + a):
        for j in range (b, 10 + b):
            if res[i][j] == 0:
                res[i][j] = 1
result = 0
for i in range (100):
    for j in range (100):
        if res[i][j] == 1:
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + x, j + y
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if res[ni][nj] == 0:
                        result += 1
                else:
                    result += 1
print(result)