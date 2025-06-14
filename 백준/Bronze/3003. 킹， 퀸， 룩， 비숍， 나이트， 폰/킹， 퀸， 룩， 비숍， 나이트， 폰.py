import sys
input = sys.stdin.readline
lst = list(map(int, input().rstrip().split()))
temp = [1,1,2,2,2,8]
res = []
for i in range (len(temp)):
    res.append(temp[i] - lst[i])
print(' '.join(map(str, res)))