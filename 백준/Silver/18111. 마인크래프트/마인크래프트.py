import sys
n, m, b = map(int, sys.stdin.readline().rstrip().split())
ground = []
for _ in range (n):
    ground.append(list(map(int, sys.stdin.readline().rstrip().split())))
res = float('inf')
min_height = min(map(min, ground))
max_hegiht = max(map(max, ground))
for target in range (min_height, max_hegiht + 1):
    inven = b
    time = 0
    for i in range(n):
        for j in range(m):
            diff = ground[i][j] - target
            if diff > 0:
                inven += diff
                time += diff * 2
            elif diff < 0:
                inven -= (-diff)
                time += (-diff)
    if inven >= 0:
        if time < res or (time==res and target > max_hegiht):
            res = time
            max_hegiht = target
print(res, max_hegiht)