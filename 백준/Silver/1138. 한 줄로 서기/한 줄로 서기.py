import sys
n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
res = [0] * n
for i in range (len(lst)):
    cnt = lst[i]
    for j in range (len(res)):
        if res[j] == 0:
            if cnt == 0:
                res[j] = i + 1
                break
            cnt -= 1
print(*res)