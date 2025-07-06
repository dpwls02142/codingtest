import sys
input = sys.stdin.readline
import math
# 08:27

n = int(input().rstrip())
lst = list(input().rstrip())
cnt = 0
for i in lst:
    if i == "O":
        cnt += 1
# print(cnt, math.ceil(n / 2))
if cnt >= math.ceil(n / 2):
    print("Yes")
else:
    print("No")