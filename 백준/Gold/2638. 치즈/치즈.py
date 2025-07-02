import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mark_air():
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    cheese[0][0] = 2

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    cheese[nx][ny] = 2
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif cheese[nx][ny] == 2:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def melt():
    melt_list = []
    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 1:
                count = 0
                for dir in range(4):
                    ni, nj = i + dx[dir], j + dy[dir]
                    if 0 <= ni < n and 0 <= nj < m and cheese[ni][nj] == 2:
                        count += 1
                if count >= 2:
                    melt_list.append((i, j))
    for x, y in melt_list:
        cheese[x][y] = 0
    return len(melt_list)

time = 0
while True:
    mark_air()
    melted = melt()
    if melted == 0:
        break
    time += 1

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 2:
                cheese[i][j] = 0

print(time)