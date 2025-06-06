import sys
input = sys.stdin.readline

n = int(input())
res = -1
oddcnt = 0
oneflag = False

for _ in range(n):
    x = int(input())
    res += x // 2 + 1
    if x % 2 == 1:
        if x == 1:
            oneflag = True
        else:
            oddcnt += 1

res += (oddcnt + 1) // 2
if oneflag and oddcnt == 0:
    res += 1

print(res)