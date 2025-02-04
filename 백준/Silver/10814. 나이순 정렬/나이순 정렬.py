import sys
n = int(sys.stdin.readline().rstrip())
c = {}

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    a = int(a)
    if a not in c:
        c[a] = [b]
    else:
        c[a].append(b)

for age in sorted(c.keys()):
    for name in c[age]:
        print(age, name)