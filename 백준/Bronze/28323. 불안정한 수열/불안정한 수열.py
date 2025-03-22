import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
first = a[0] % 2 # 0
# 짝+홀, 홀+짝
cnt = 1
for i in range (1, len(a)):
    if a[i] % 2 == 1 - first:
        cnt += 1
        first = 1 - first
print(cnt)