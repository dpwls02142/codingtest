import sys

n, a, b = map(int, sys.stdin.readline().rstrip().split())
tile_1x2 = list(map(int, sys.stdin.readline().rstrip().split()))  # 2x1, 1x2 사각형
tile_2x2 = list(map(int, sys.stdin.readline().rstrip().split()))  # 2x2 사각형

tile_1x2.sort()
tile_2x2.sort()

max_pretty = 0

if n % 2 != 0:
    max_pretty += tile_1x2[-1]
    tile_1x2.pop()
    n -= 1

for i in range (0, n, 2):
    t1, t2 = 0, 0
    if len(tile_1x2) >= 2:
        t1 = tile_1x2[-1] + tile_1x2[-2]
    if len(tile_2x2) >= 1:
        t2 = tile_2x2[-1]
    if t1 > t2:
        max_pretty += t1
        tile_1x2.pop()
        tile_1x2.pop()
    else:
        max_pretty += t2
        tile_2x2.pop()

print(max_pretty)