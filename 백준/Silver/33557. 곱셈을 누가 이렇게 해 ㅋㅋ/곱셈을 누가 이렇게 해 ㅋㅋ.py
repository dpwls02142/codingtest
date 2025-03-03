import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    max_int = max(len(a), len(b))
    t = 0
    if max_int == len(a):
        t = len(a) - len(b)
        b = b.zfill(max_int)
    else:
        t = len(b) - len(a)
        a = a.zfill(max_int)

    strange = ""
    for i in range (t):
        if a[i] == "0":
            strange += b[i]
        elif b[i] == "0":
            strange += a[i]

    for i in range(t, max_int):
        a_temp = int(a[i])
        b_temp = int(b[i])
        strange += str(int(a[i]) * int(b[i]))

    # print(strange)
    # print((int(a) * int(b)))

    if str(int(a) * int(b)) == strange:
        print(1)
    else:
        print(0)