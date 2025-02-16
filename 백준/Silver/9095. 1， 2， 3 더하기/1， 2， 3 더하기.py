import sys

t = int(sys.stdin.readline().rstrip())

dp = [0] * 12
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range (3, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range (t):
    a = int(sys.stdin.readline().rstrip())
    print(dp[a-1])