import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
temp = list(map(int, input().rstrip().split()))
t = sum(temp[:k])
res = t
for i in range (k, n):
    t += temp[i] - temp[i - k]
    res = max(res, t)
print(res)