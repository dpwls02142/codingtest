import sys
from decimal import Decimal

x, y = map(int, sys.stdin.readline().rstrip().split())
before_z = int(Decimal(y) / Decimal(x) * 100)

if before_z >= 99:
    print(-1)
else:
    low = 0
    high = x
    res = -1
    while low <= high:
        mid = (low + high) // 2
        curr_z = int(Decimal(y + mid) / Decimal(x + mid) * 100)
        if curr_z > before_z:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    print(res)