import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1 

while b > a:
    if b % 2 == 0:
        b //= 2
    elif str(b)[-1] == '1':
        b = int(str(b)[:-1])
    else:
        cnt = -1
        break
    cnt += 1 

if b == a:
    print(cnt)
else:
    print(-1)