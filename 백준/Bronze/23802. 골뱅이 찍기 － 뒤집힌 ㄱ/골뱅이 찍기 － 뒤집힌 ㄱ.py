import sys
input = sys.stdin.readline

n = int(input().rstrip())
for _ in range (n):
    print("@" * (5 * n))
for _ in range(4 * n):
    print("@" * n)
