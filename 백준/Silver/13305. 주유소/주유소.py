import sys

n = int(sys.stdin.readline().rstrip()) 
city = list(map(int, sys.stdin.readline().rstrip().split()))
coin = list(map(int, sys.stdin.readline().rstrip().split()))

res = 0
min_coin = coin[0]

for i in range(n - 1):
    min_coin = min(min_coin, coin[i])
    res += min_coin * city[i]

print(res)