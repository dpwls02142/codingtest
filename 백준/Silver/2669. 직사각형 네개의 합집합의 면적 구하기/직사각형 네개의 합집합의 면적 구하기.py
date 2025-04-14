import sys
rect = set()
for _ in range (4):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().rstrip().split())
    for x in range (left_x, right_x):
        for y in range (left_y, right_y):
            rect.add((x, y))
print(len(rect))