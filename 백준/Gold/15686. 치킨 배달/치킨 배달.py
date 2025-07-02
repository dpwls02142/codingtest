import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().rstrip().split())
city = []
for i in range (n):
    city.append(list(map(int, input().rstrip().split())))
house, chicken = [], []
for i in range (n):
    for j in range (n):
        if city[i][j] == 1:
            house.append((i+1, j+1))
        if city[i][j] == 2:
            chicken.append((i+1, j+1))
res = float('inf')
for select_chicken in combinations(chicken, m):
    distance = 0
    for hx, hy in house:
        min_distance = float('inf')
        for cx, cy in select_chicken:
            dist = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, dist)
        distance += min_distance
    res = min(distance, res)
print(res)