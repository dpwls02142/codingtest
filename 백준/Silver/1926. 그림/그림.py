import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
draw = []
for _ in range(n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    draw.append(a)

cnt = 0 # 그림 개수
res = [0] # 그림 넓이를 저장할 리스트

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append([x, y]) # 0, 0
    draw[x][y] = 0 # 방문한 노드는 0으로 초기화
    b = 1 # 넓이를 계산하기 위한 변수
    while queue: # queue 안에 원소가 있을 때 까지
        c, d = queue.popleft() # c에 0, d에 0
        for i in range (4): # i가 1일 때
            nx = c + dx[i] # 0 + 0
            ny = d + dy[i] # 0 + 0
            if (0 <= nx < n) and (0 <= ny < m) and (draw[nx][ny] == 1):
                b += 1
                draw[nx][ny] = 0
                queue.append([nx, ny])
    res.append(b)

for x in range (n):
    for y in range (m):
        if draw[x][y] == 1: # draw 안에 1이 있을 때만
            bfs(x, y) # bfs 함수를 호출하고
            cnt += 1 # 그림의 개수를 +1씩 증가

print(cnt)
print(max(res))