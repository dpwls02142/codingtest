import sys
input = sys.stdin.readline

x = int(input())
y = sum(int(n) for n in str(x))
if len(str(y)) > 1:
    cnt = 1
    while len(str(y)) > 1:
        y = sum(int(n) for n in str(y))
        cnt += 1
    print(cnt)
    if y % 3 == 0:
        print("YES")
    else:
        print("NO")
else:
    print(0)
    if y % 3 == 0:
        print("YES")
    else:
        print("NO")