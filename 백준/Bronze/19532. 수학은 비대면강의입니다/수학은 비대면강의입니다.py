import sys
a, b, c, d, e, f = list(map(int,sys.stdin.readline().rstrip().split()))

det = a * e - b * d

x = (c * e - b * f) // det
y = (a * f - c * d) // det
print(x, y)