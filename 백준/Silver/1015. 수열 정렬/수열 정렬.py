import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

indexed_a = []
for i in range(n):
    indexed_a.append((a[i], i))
indexed_a.sort()

p = [0] * n

for i in range(n):
    value, ori_index = indexed_a[i]
    p[ori_index] = i

print(' '.join(map(str, p)))