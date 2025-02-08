import sys
n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(0)
    exit(0)
    
a = [0] * (10000000 + 1)

for i in range (2, n + 1):
    a[i] = a[i-1] + 1
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2]+1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3]+1)
        
print(a[n])