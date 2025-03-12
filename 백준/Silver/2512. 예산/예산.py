import sys

# 이진탐색은 특정값을 빠르게 찾아야 될 때 뿐만 아니라,
# "최적의 값"을 탐색해야 될 때도 사용한다.

n = int(sys.stdin.readline().rstrip())
money = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

low_money = 0
high_money = max(money)
res = 0

while low_money <= high_money:
    maximum_amount = (low_money + high_money) // 2
    total = 0

    for i in money:
        total += min(i, maximum_amount)
    
    if total > m:
        high_money = maximum_amount - 1
    else:
        res = maximum_amount
        low_money = maximum_amount + 1

print(res)