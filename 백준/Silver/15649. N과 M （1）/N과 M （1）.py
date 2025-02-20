import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
ans = []
def back(n):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range (1, n+1):
        if i not in ans:
            ans.append(i)
            back(n)
            ans.pop()
back(n)