b = []
c = []
res = []

for x in range (0, 10):
    a = int(input())
    c.append(a)

    b = c[x] % 42

    if b not in res:
        res.append(b)
    elif b in res:
        continue

print(len(res))