import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
room = []
for i in range (n):
    room.append(list(map(int, input().rstrip().split())))
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0
while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1
    cleaned = False
    for i in range (4):
        d = (d + 3) % 4
        ny = r + dy[d]
        nx = c + dx[d]
        if 0 <= ny < n and 0 <= nx < m and room[ny][nx] == 0:
            r, c = ny, nx
            cleaned = True
            break
    if not cleaned:
        back = (d + 2) % 4
        br = r + dy[back]
        bc = c + dx[back]
        if room[br][bc] == 1:
            break
        else:
            r, c = br, bc
print(cnt)