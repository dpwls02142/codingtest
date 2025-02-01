import sys

b = []

for i in range (9):
    a = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    b.append(a)

max_int = -1
max_x = 0
max_y = 0

for i in range(len(b)):
    for j in range(len(b[i])):
        if max_int < b[i][j]:
            max_int = b[i][j]
            max_x = i + 1
            max_y = j + 1

print(max_int)
print(max_x, max_y)