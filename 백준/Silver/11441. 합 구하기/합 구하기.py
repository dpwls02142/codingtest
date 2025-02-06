import sys
# 매 구간마다 합을 각각 구하면 O(n)의 시간이 걸리기 때문에,
# d에 미리 누적합을 구해놔서, 연산을 하는게 빠름.

a = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))
c = int(sys.stdin.readline().rstrip())

d = [0] * (a + 1)
for i in range(1, a + 1):
    d[i] = d[i - 1] + b[i - 1]

for _ in range(c):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(d[j] - d[i - 1])
