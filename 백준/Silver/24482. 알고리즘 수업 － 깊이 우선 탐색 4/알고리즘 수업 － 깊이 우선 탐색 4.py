import sys

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u) 

# 내림차순 방문을 위해 오름차순 정렬
# stack은 LIFO 구조이기에 오름차순으로 정렬해야, 내림차순으로 원소가 출력됨
for i in range(1, n + 1):
    graph[i].sort()

# 방문 하지 않은 경우에 -1을 출력해야 되니까
depth = [-1] * (n + 1)
# (시작 정점, 깊이) 저장
stack = [(r, 0)]
while stack:
    node, d = stack.pop()
    if depth[node] == -1:
        depth[node] = d
        for next_node in graph[node]:
            if depth[next_node] == -1:
                stack.append((next_node, d + 1))

for i in range(1, n + 1):
    print(depth[i])