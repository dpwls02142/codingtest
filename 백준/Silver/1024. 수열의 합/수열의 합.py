import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())

found = False
for k in range(L, 101):
    temp = N - k * (k - 1) // 2
    if temp < 0:
        break
    if temp % k == 0:
        x = temp // k
        if x >= 0:
            result = [str(x + i) for i in range(k)]
            print(" ".join(result))
            found = True
            break

if not found:
    print(-1)