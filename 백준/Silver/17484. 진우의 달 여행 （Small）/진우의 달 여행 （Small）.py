import sys

n, m = map(int, sys.stdin.readline().strip().split())
space = []
for _ in range(n):
    space.append(list(map(int, sys.stdin.readline().strip().split())))

# dp[i][j][k]: i번째 행, j번째 열, k 방향에서의 최소 연료
# k = 0: 왼쪽 대각선에서 옴, k = 1: 아래에서 옴, k = 2: 오른쪽 대각선에서 옴
dp = [[[float('inf') for _ in range(3)] for _ in range(m)] for _ in range(n)]

for j in range(m):
    for k in range(3):
        dp[0][j][k] = space[0][j]

for i in range(1, n):
    for j in range(m):
        # 왼쪽 대각선으로 이동 (k=0)
        if j + 1 < m:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + space[i][j]
        
        # 수직으로 이동 (k=1)
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i][j]
        
        # 오른쪽 대각선으로 이동 (k=2)
        if j - 1 >= 0:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + space[i][j]
# print(dp)
result = float('inf')
for j in range(m):
    result = min(result, min(dp[n-1][j]))
print(result)