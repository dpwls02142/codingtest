import sys

n = int(input())
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\\$%*+-./:"
res = ""

for _ in range (0, n):
    a = list(sys.stdin.readline().rstrip().split(" "))
    r = int(a[0])
    t = list(a[1])

    for char in t:
        if char in s:
            res = char * r
            print(res, end = '')
    print()