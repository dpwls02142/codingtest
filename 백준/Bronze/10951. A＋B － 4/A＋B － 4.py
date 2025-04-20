import sys
input = sys.stdin.readline
try:
    while True:
        a, b = map(int, input().split())
        print(a + b)
except ValueError:
    sys.exit()