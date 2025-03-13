import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
desk = list(sys.stdin.readline().rstrip())
res = 0

for i in range(n):
    if desk[i] == 'P':
        for j in range(max(0, (i - k)), min(n, (i + k + 1))):
            if desk[j] == 'H':
                desk[j] = 'E'
                res += 1
                break

print(res)