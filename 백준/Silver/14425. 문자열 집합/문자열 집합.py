import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
search, find = set(), []
for _ in range (n):
    search.add(input().rstrip())
for _ in range (m):
    find.append(input().rstrip())
cnt = 0
for i in find:
    if i in search:
        cnt += 1
print(cnt)