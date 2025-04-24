import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = []
for _ in range (n):
    m.append(int(input().rstrip()))
if n <= 1:
    print(0)
else:
    res = 0
    while True:
        max_m = max(m[1:])
        if m[0] > max_m:
            break
        idx = m[1:].index(max_m) + 1
        m[idx] -= 1
        m[0] += 1
        res += 1
    print(res)