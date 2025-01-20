import sys

a = list(sys.stdin.readline().rstrip().split(" "))

b = list(a[0])
c = list(b)

d = list(a[1])
e = list(d)

if (b != d):
    b[0] = c[2]
    b[2] = c[0]

    d[0] = e[2]
    d[2] = e[0]

if (b >= d):
    print(*b, sep='')
else:
    print(*d, sep='')