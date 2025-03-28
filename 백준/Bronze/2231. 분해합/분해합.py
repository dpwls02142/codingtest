import sys
n = int(sys.stdin.readline().rstrip())
for i in range (0, n):
    res = 0
    temp = i
    while temp > 0:
        res += temp % 10
        temp //= 10
    res += i
    if res == n:
        print(i)
        break
else:
    print(0)