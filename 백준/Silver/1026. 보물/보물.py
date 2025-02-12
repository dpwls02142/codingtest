import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

res = 0

for i in range (n):
    res += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(res)