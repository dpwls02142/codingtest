import sys
N = int(sys.stdin.readline().rstrip())
for i in range (N - 1):
    print(" " * (i) + "*" * ((N * 2) - (i + (1 + i))))
for i in range (N):
    print(" " * (N - (i + 1)) + "*" * ((i * 2) + 1))