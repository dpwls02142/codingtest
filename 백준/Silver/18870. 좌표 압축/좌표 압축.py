import sys
input = sys.stdin.readline
n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
b = sorted(set(a))
c = {}
for idx, value in enumerate(b):
    c[value] = idx
res = []
for i in a:
    res.append(c[i])
print(' '.join(map(str, res)))