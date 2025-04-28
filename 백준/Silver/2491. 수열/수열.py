import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
inc, dec, res = 1, 1, 1

for i in range (1, n):
    if seq[i] >= seq[i-1]:
        inc += 1
    else:
        inc = 1
    
    if seq[i] <= seq[i-1]:
        dec += 1
    else:
        dec = 1
    
    res = max(res, inc, dec)
print(res)