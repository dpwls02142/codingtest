import sys
input = sys.stdin.readline
n = int(input().rstrip())
e = int(input().rstrip())
members = []
for i in range (e):
    a = list(map(int, input().rstrip().split()))
    members.append(a[1:])
res = {x: [] for x in range(1, n + 1)}
cnt = 0
for i in range (e):
    if 1 in members[i]:
        for x in members[i]:
            res[x].append(cnt)
        cnt += 1
    else:
        s = set()
        for x in members[i]:
            s.update(res[x])
        for x in members[i]:
            res[x] = list(s)
# print(res)
for idx in range(1, n + 1):
    if len(res[idx]) == cnt:
        print(idx)