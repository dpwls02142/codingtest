import sys
import math
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range (t):
    x1, y1, r1, x2, y2, r2 = map(int, input().rstrip().split())
    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    if d == 0 and r1 == r2:
        print(-1)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    else:
        print(0)