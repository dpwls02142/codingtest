import sys
input = sys.stdin.readline
from collections import deque
n = int(input().rstrip())
res = {}
for i in range (1, n + 1):
    res[i] = []
for _ in range (n-1):
    a, b = map(int, input().rstrip().split())
    res[b].append(a)
    res[a].append(b)

parent = [0] * (n + 1)
visited = [False] * (n + 1)

queue = deque([1])
visited[1] = True

while queue:
    cur = queue.popleft()
    for sibling in res[cur]:
        if not visited[sibling]:
            parent[sibling] = cur
            visited[sibling] = True
            queue.append(sibling)

for i in range (2, n + 1):
    print(parent[i])