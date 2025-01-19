import sys

n = int(input())
b = list(map(int, sys.stdin.readline().rstrip().split(" ")))
a = b[0]

score = []
res, res2 = 0, 0

for i in range (1, n):
    if b[i] > a:
        a = b[i]

for j in range (0, n):

    res = b[j]/a*100
    score.append(res)

    res2 += score[j]

res2 /= n

print(res2)