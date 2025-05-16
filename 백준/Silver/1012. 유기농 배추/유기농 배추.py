import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x, y, field, visited, n, m):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if field[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((nx, ny))


t = int(input().rstrip())
for _ in range (t):
    m, n, k = map(int, input().rstrip().split())
    field = [[0] * m for _ in range (n)]
    visited = [[False] * m for _ in range (n)]
    
    for _ in range (k):
        x, y = map(int, input().rstrip().split())
        field[y][x] = 1

    cnt = 0
    for i in range (n):
        for j in range (m):
            if field[i][j] == 1 and not visited[i][j]:
                bfs(j, i, field, visited, n, m)
                cnt += 1

    print(cnt)
