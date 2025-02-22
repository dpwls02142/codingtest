import sys

n = int(sys.stdin.readline().rstrip())

for _ in range (n):
    res = 0
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    t = a[0]
    s = a[1:]
    for i in range(1, len(s)):
        while (i > 0) and (s[i] < s[i - 1]):
            s[i], s[i - 1] = s[i - 1], s[i]
            res += 1
            i -= 1
    print(t, res)