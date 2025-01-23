a = input().split(" ")
b, c = int(a[0]), int(a[1])
d2, e2, res = [], [], []

for i in range(b):
    d = list(map(int, input().split(" ")))
    d2.append(d)

for i in range(b):
    e = list(map(int, input().split(" ")))
    e2.append(e)

for i in range (b):
    row = []
    for j in range(c):
        row.append(d2[i][j] + e2[i][j])
    res.append(row)

for row in res:
    print(*row)