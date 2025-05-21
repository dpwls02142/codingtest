import sys
input = sys.stdin.readline
h, w, x, y = map(int, input().rstrip().split())
a = [[0 for _ in range (w)] for _ in range (h)]
b = []
for _ in range (h + x):
    b.append(list(map(int, input().rstrip().split())))
for i in range (h):
    for j in range (w):
        if i >= x and j >= y:
            a[i][j] = b[i][j] - a[i-x][j-y]
        else:
            a[i][j] = b[i][j]
for i in a:
    print(' '.join(map(str, i)))