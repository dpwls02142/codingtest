import sys
input = sys.stdin.readline
from collections import Counter
n, m = map(int, input().rstrip().split())
ori = []
for _ in range (n):
    ori.append(input().rstrip())
res = ""
for i in range (m):
    col = []
    for j in range (n):
        col.append(ori[j][i])
    col_cnt = Counter(col)
    temp = sorted(col_cnt.items(), key=lambda x: (-x[1], x[0]))
    res += temp[0][0]
print(res)
cnt = 0
for i in ori:
    for j in range (m):
        if i[j] != res[j]:
            cnt += 1
print(cnt)