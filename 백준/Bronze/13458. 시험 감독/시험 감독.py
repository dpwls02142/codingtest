import sys
import math
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, sys.stdin.readline().rstrip().split())
cnt = 0
for i in range(len(a)):
    a[i] -= b # 5 - 2 = 3
    cnt += 1
    if a[i] <= 0:
        continue
    if a[i] > 0:
        cnt += math.ceil(a[i] / c)
print(cnt)