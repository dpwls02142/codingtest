import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
if (m // n) % 2 == 1:
    print(n - m % n)
else:
    print(m % n)