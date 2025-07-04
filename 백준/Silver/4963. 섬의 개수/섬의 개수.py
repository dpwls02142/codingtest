import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

dy = [-1, -1, -1, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, -1, 0, 1, -1, 1]
def dfs(y, x):
    lst[y][x] = 0
    for i in range (8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and lst[ny][nx] == 1:
            dfs(ny, nx)

while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    else:
        cnt = 0
        lst = []
        for i in range (h):
            lst.append(list(map(int, input().rstrip().split())))
        for i in range (h):
            for j in range (w):
                if lst[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
        print(cnt)