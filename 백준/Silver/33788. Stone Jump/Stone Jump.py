import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    if n == 1 or (s[0] != 'L' or s[-1] != 'R'):
        print("YES")
    else:
        print("NO")
