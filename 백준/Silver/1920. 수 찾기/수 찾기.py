import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()

for i in range (len(b)):
    left = 0
    right =  n-1
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == b[i]:
            res = 1
            break
        elif a[mid] < b[i]:
            left = mid + 1
        else:
            right = mid - 1
    print(res)