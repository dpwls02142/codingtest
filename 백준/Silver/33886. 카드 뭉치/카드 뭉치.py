import sys
input = sys.stdin.readline
n = int(input().rstrip())
cards = list(map(int, input().rstrip().split()))

dp = [float('inf')] * (n + 1)
dp[n] = 0

for i in range(n - 1, -1, -1):
    max_len = cards[i]
    for length in range(1, max_len + 1):
        if i + length <= n:
            dp[i] = min(dp[i], 1 + dp[i + length])
print(dp[0])