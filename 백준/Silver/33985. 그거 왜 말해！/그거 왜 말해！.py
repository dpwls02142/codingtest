import sys
input = sys.stdin.readline
n = int(input().rstrip())
t = input().rstrip()

if t[0] == 'A' and t[-1] == 'B':
    print('Yes')
else:
    print('No')