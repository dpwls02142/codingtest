import sys
s = str(sys.stdin.readline().rstrip())
a = int(sys.stdin.readline().rstrip())
for i in range (a):
    a = ""
    b, c, d = map(str, sys.stdin.readline().rstrip().split())
    a = s[int(c):(int(d)+1)]
    print(a.count(b))