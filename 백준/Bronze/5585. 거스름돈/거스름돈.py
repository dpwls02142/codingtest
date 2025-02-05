import sys

cash = int(sys.stdin.readline().rstrip())
a = 1000 - cash

cnt = 0

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    cnt += a // coin
    a %= coin

print(cnt)