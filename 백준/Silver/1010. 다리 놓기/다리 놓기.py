import sys
import math

t = int(sys.stdin.readline().rstrip())
for _ in range (t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    res = math.comb(m, n)
    print(res)