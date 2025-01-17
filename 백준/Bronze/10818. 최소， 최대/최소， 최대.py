import sys

n = int(input())
x = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(min(x),max(x))