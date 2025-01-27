import sys

b = []
res = []

for i in range (3):
    a = list(sys.stdin.readline().rstrip().split(" "))
    b.append(a)

if b[0][0] == b[1][0]:
    res.append(b[2][0])
elif b[0][0] == b[2][0]:
    res.append(b[1][0])
else:
    res.append(b[0][0])

if b[0][1] == b[2][1]:
    res.append(b[1][1])
elif b[0][1] == b[1][1]:
    res.append(b[2][1])
else:
    res.append(b[0][1])

print(' '.join(res))