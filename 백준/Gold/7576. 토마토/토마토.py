import sys
input = sys.stdin.readline
from collections import deque
def bfs(m, n, box):
    q = deque()
    for x in range (n):
        for y in range (m):
            if box[x][y] == 1:
                q.append((y, x))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                q.append((nx, ny))
    day = 0
    for r in box:
        for v in r:
            if v == 0:
                return -1
            day = max(day, v)
    return day - 1
            
m, n = map(int, input().rstrip().split())
box = []
for _ in range (n):
    box.append(list(map(int, input().rstrip().split())))
print(bfs(m, n, box))