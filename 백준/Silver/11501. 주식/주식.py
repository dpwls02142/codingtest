import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    day = int(sys.stdin.readline().rstrip())
    stock = list(map(int, sys.stdin.readline().rstrip().split()))
    max_price = 0 
    res = 0
    for i in range(day - 1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            res += max_price - stock[i]
    print(res)