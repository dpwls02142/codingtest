import sys
from collections import deque
input = sys.stdin.readline
n = int(input().rstrip())
fish = [list(map(int, input().split())) for _ in range (n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(start, size, n, space):
    q = deque([(start[0], start[1], 0)])
    visit = [[0] * n for _ in range(n)]
    visit[start[0]][start[1]] = 1
    fish = []
    
    while q:
        x, y, dist = q.popleft()
        if space[x][y] != 0 and space[x][y] < size:
            fish.append((dist, x, y))
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if space[nx][ny] <= size:
                    visit[nx][ny] = True
                    q.append((nx, ny, dist + 1))
    return fish

def solve(n, space):
    start = None
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                start = (i, j, 0)
                space[i][j] = 0 
                break

    size = 2
    eaten = 0 
    time = 0

    while True:
        fish = bfs(start[:2], size, n, space)
        if not fish:
            break

        fish.sort()
        dist, fx, fy = fish[0]

        time += dist
        space[fx][fy] = 0
        start = (fx, fy, dist)

        eaten += 1
        if eaten == size:
            size += 1
            eaten = 0
    return time

print(solve(n, fish))