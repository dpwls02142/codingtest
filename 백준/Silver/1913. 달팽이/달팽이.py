import sys
input = sys.stdin.readline

n = int(input().rstrip())
find = int(input().rstrip())

lst = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n // 2, n // 2
lst[x][y] = 1
val = 2
step = 1
fx, fy = 0, 0

if find == 1:
    fx, fy = x + 1, y + 1

while val <= n * n:
    for d in range(4):
        for _ in range(step):
            if val > n * n:
                break
            x += dx[d]
            y += dy[d]
            lst[x][y] = val
            if val == find:
                fx, fy = x + 1, y + 1
            val += 1
        if d % 2 == 1:
            step += 1

for row in lst:
    print(' '.join(map(str, row)))
print(fx, fy)