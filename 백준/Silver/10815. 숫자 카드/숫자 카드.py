import sys

a = int(sys.stdin.readline().rstrip()) # n 개수
n = list(sys.stdin.readline().rstrip().split(" "))

b = int(sys.stdin.readline().rstrip()) # m 개수
m = list(sys.stdin.readline().rstrip().split(" "))

n_set = set(n)
res = []

for number in m:
    if number in n_set:
        res.append('1')
    else:
        res.append('0')

print(' '.join(res))