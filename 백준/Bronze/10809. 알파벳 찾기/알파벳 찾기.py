import sys
input = sys.stdin.readline
s = input().rstrip()
lst = ['a', 'b', 'c', 'd', 'e', 'f', 
       'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r',
       's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in lst:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')