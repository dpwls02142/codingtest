import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

b = []
for _ in range (n):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b.append(a)

b.sort(key=lambda x: (-x[1], -x[2], -x[3]))

rank = 1 
for i in range(n):
    if i > 0 and b[i][1:] == b[i-1][1:]:
        pass
    else:
        rank = i + 1
    if b[i][0] == k:
        print(rank)
        break