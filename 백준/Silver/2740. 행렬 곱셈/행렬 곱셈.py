import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
vector_a = []
for _ in range (n):
    vector_a.append(list(map(int, sys.stdin.readline().rstrip().split())))
m, k = map(int, sys.stdin.readline().rstrip().split())
vector_b = []
for _ in range (m):
    vector_b.append(list(map(int, sys.stdin.readline().rstrip().split())))
res = [[0] * k for _ in range (n)]
for c in range (k):
    for i in range (n):
        temp = 0
        for j in range (m):
            temp += vector_a[i][j] * vector_b[j][c]
        res[i][c] = temp
# matrix = [[0] * n for _ in range(k)]
# for i in range(len(res)):
#     col = i // k
#     row = i % k
#     matrix[row][col] = res[i]
# for row in matrix:
#     print(*row)
# print(res)
for i in res:
    print(' '.join(map(str, i)))