import sys
input = sys.stdin.readline
t = int(input().rstrip())
lst = []
cnt = 1
for i in range (t):
    lst.append(int(input().rstrip()))
a = lst[-1]
for i in range (t-1, -1, -1):
    if a < lst[i]:
        cnt += 1
        a = lst[i]
print(cnt)