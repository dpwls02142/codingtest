import sys
n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
if n <= k:
    print(0)
else:
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    lst.sort()
    temp = []
    for i in range (n-1):
        temp.append(lst[i+1] - lst[i])
    temp.sort()
    i = 0
    while i < k-1:
        temp.pop()
        i += 1
    print(sum(temp))