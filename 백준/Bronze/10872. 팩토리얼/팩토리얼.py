import sys
a = int(sys.stdin.readline().rstrip())
res = 1
for i in range (1, a+1):
    res *= i
print(res)