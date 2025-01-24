import sys

res = []

for _ in range (5):
    a = list(sys.stdin.readline().rstrip())
    res.append(a)

max_length = max(len(row) for row in res)

for i in range(max_length):
    for j in range(len(res)):
        if i < len(res[j]):
            print(res[j][i], end='')