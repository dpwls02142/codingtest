import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

if n == m:
    side = n - 1
    inner_points = (side - 1) * (side - 1)
    boundary_points = 4
    print(inner_points + (boundary_points // 2) - 1)
else:
    side = min(n, m) - 1
    inner_points = (side - 1) * (side - 1)
    boundary_points = 4 + 4 * (side - 1)
    print(inner_points + (boundary_points // 2) - 1)