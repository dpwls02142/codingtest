import sys

n = int(input())
a = list(map(int,sys.stdin.readline().rstrip().split(" ")))
v = int(input())
res = 0

for j in range(0, n):
    if (v == int(a[j])):
        res += 1

print(res)