from itertools import combinations
from collections import deque
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1,0), (1,0), (0,-1), (0,1)]
empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def spread_virus(labc):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and labc[nx][ny] == 0:
                labc[nx][ny] = 2
                queue.append((nx, ny))

def safe(labc):
    return sum(row.count(0) for row in labc)

res = 0
for walls in combinations(empty, 3):
    labc = [row[:] for row in lab]
    for x, y in walls:
        labc[x][y] = 1
    spread_virus(labc)
    res = max(res, safe(labc))

print(res)