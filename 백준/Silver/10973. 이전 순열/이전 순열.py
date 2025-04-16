import sys
N = int(sys.stdin.readline().rstrip())
per = list(map(int, sys.stdin.readline().rstrip().split()))
temp = [x for x in range (1, N+1)]
if per == temp:
    print(-1)
else:
    i = N - 2
    while i >= 0 and per[i] <= per[i+1]:
        i -= 1
    j = N - 1
    while per[j] >= per[i]:
        j -= 1
    per[i], per[j] = per[j], per[i]
    per[i+1:] = reversed(per[i+1:])
    print(" ".join(map(str, per)))