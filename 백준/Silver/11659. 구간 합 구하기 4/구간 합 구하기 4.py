import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
res = [0 for _ in range (n + 1)]
for i in range (1, n + 1):
    res[i] = res[i-1] + lst[i-1]
# print(res)
for _ in range (m):
    i, j = map(int, input().rstrip().split())
    print(res[j] - res[i-1])