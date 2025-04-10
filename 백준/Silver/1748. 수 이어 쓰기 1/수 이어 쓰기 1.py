import sys
n = int(sys.stdin.readline().rstrip())
res = 0
length, start = 1, 1
while start * 10 <= n:
    end = start * 10 - 1
    res += (end - start + 1) * length
    start *= 10
    length += 1
res += (n-start+1)*length
print(res)