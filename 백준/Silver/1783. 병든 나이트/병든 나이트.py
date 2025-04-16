import sys
N, M = map(int, sys.stdin.readline().strip().split())
if N == 1:
    print(1)
elif N == 2:
    print(min(4, ((M + 1) // 2)))
elif M < 7:
    print(min(4, M))
else:
    print(M - 7 + 5)