import sys
input = sys.stdin.readline
n = int(input().rstrip())
wallet = []
for _ in range (n):
    money = int(input().rstrip())
    if money <= 500 or money >= 20000:
        continue
    else:
        wallet.append(money - 500)

dp = [-1] * 500
dp[0] = 0
for w in wallet:
    ndp = dp[:]
    for r in range(500):
        if dp[r] != -1:
            new_sum = dp[r] + w
            ndp[new_sum % 500] = max(ndp[new_sum % 500], new_sum)
    dp = ndp

if dp[0] != 0:
    print(dp[0])
else:
    print(0)