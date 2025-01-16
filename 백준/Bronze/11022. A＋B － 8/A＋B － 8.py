import sys

t = int(input())

for i in range (1, t+1):
    a = sys.stdin.readline().rstrip().split(" ")  # 문자열 반환

    b = int(a[0])
    c = int(a[1])

    if (0 < b, c < 10):
        res = b + c
        print("Case #%d: %d + %d = %d" % (i, b, c, res))