import sys
input = sys.stdin.readline
from collections import deque
puyo = []
col = 0
for i in range (12):
    puyo.append(list(input().rstrip()))
col = len(puyo[0])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs (x, y, c, v):
    q = deque()
    q.append((x, y))
    v[y][x] = True
    connected = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for i in range (4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < col and 0 <= ny < 12:
                if not v[ny][nx] and puyo[ny][nx] == c:
                    v[ny][nx] = True
                    q.append((nx, ny))
                    connected.append((nx, ny))
    return connected

def gravity():
    for x in range (col):
        q = deque()
        for y in range (11, -1, -1):
            if puyo[y][x] != '.':
                q.append(puyo[y][x])
        for y in range(11, -1, -1):
            if q:
                puyo[y][x] = q.popleft()
            else:
                puyo[y][x] = '.'

res = 0
while True:
    visited = [[False]*col for _ in range(12)]
    to_pop = set()

    for y in range(12):
        for x in range(col):
            if puyo[y][x] != '.' and not visited[y][x]:
                group = bfs(x, y, puyo[y][x], visited)
                if len(group) >= 4:
                    to_pop.update(group)

    if not to_pop:
        break

    for x, y in to_pop:
        puyo[y][x] = '.'

    gravity()
    res += 1

print(res)
