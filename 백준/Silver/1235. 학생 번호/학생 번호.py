import sys
input = sys.stdin.readline
t = int(input().rstrip())
lst = []
for _ in range (t):
    lst.append(input().rstrip())
for i in range (1, len(lst[0])+1):
    s = set()
    for j in lst:
        s.add(j[-i:])
    if len(s) == t:
        print(i)
        break