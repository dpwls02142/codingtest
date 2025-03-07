from collections import deque
import sys

n, m, start_pos = map(int, sys.stdin.readline().rstrip().split())
graph =[[False] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(start_pos):
    visited1[start_pos] = True
    print(start_pos, end=" ")
    for i in range(1, n + 1):
        if not visited1[i] and graph[start_pos][i] == 1:
            dfs(i)

def bfs(start_pos):
    q = deque([start_pos])
    visited2[start_pos] = True
    while q:
        start_pos = q.popleft()
        print(start_pos, end=" ")
        for i in range(1, n + 1):
            if not visited2[i] and graph[start_pos][i] == 1:
                q.append(i)
                visited2[i] = True
dfs(start_pos)
print()
bfs(start_pos)

"""
input:
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

# 1: [2, 3, 4]
# 2: [1, 4]
# 3: [1, 4]
# 4: [1, 2, 3]
# DFS(Stack): 1 - 2 - 4 - 3 : 작은 번호의 노드를 우선 방문
# BFS(Queue): 1 - 2 - 3 - 4 : 현재 노드에서 갈 수 있는 모든 노드를 방문 후 그 다음 레벨로