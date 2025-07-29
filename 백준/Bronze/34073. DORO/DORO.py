import sys
input = sys.stdin.readline

n = int(input())
doro = list(input().rstrip().split())
res = []
for i in range (n):
    res.append(doro[i] + "DORO")
print(" ".join(res))