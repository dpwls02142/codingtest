import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
x = [_ for _ in range (1, n+1)]
res = []
idx = 0

while x:
    idx = (idx + k - 1) % len(x)
    res.append(str(x.pop(idx)))

print("<" + ", ".join(res) + ">")