import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())

horizontal_cuts = [0, y]
vertical_cuts = [0, x]

for _ in range(n):
    direction, line = map(int, input().split())
    if direction == 0:
        horizontal_cuts.append(line)
    else:
        vertical_cuts.append(line)

horizontal_cuts.sort()
vertical_cuts.sort()

max_height = 0
for i in range(1, len(horizontal_cuts)):
    height = horizontal_cuts[i] - horizontal_cuts[i-1]
    max_height = max(max_height, height)

max_width = 0
for i in range(1, len(vertical_cuts)):
    width = vertical_cuts[i] - vertical_cuts[i-1]
    max_width = max(max_width, width)

print(max_width * max_height)