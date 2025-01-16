t = int(input())

for i in range(0, t):
    a = input().split(" ")

    su1 = int(a[0])
    su2 = int(a[1])

    if (su1 > 0 and su2 < 10):
        res = su1 + su2
        print(res)