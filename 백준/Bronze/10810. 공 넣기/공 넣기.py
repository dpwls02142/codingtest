import sys

n = list(map(int, sys.stdin.readline().rstrip().split(" ")))
a = n[0]
b = []
m = n[1]

if ( 1 <= a,m <=100 ):
    for i in range (0, a):
        b.append(0)
    for _ in range (0, m):
        c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        d = c[0]
        e = c[1]
        f = c[2]
        for g in range (d-1, e):
            b[g] = f

print(*b, sep=' ')