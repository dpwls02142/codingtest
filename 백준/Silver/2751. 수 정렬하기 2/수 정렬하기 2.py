import sys

n = int(sys.stdin.readline())
res = []

for i in range(n):
    a = int(sys.stdin.readline())
    res.append(a)

res.sort()

for num in res:
    print(num)
