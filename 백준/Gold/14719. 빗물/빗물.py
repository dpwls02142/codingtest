import sys
input = sys.stdin.readline
h, w = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
block = [[0] * w for _ in range (h)]
for x in range (w):
    for y in range (1, lst[x]+1):
        block[-y][x] = 1
left_max = [0] * w
right_max = [0] * w
left_max[0] = lst[0]
for i in range(1, w):
    left_max[i] = max(left_max[i-1], lst[i])
right_max[-1] = lst[-1]
for i in range(w-2, -1, -1):
    right_max[i] = max(right_max[i+1], lst[i])
water = [0] * w
for i in range(w):
    water[i] = max(0, ((min(left_max[i], right_max[i])) - lst[i]))
print(sum(water))