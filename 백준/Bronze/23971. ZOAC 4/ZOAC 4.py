import sys
h, w, n, m = map(int, sys.stdin.readline().rstrip().split())

rows = (h + n) // (n + 1) # 3
cols = (w + m) // (m + 1) # 2

cnt = rows * cols # 6
print(cnt)