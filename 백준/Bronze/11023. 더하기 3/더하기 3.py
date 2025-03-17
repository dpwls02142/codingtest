import sys
a = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
for i in a:
    res += i
print(res)
# print(sum(a))