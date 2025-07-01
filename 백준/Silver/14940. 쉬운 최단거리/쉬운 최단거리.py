from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, grid, distance, n, m):
    queue = deque()
    queue.append((start_x, start_y))
    distance[start_x][start_y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_x, start_y = i, j

bfs(start_x, start_y, grid, distance, n, m)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()