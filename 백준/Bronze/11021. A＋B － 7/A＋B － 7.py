t = []
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    t.append((a, b))

for i, (a, b) in enumerate(t):
    res = a + b
    print("Case #%d: %d" % (i+1, res))