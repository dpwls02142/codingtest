import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
listen, seen = set(), set()
for _ in range (n):
    listen.add(input().rstrip())
for _ in range (m):
    seen.add(input().rstrip())

res = listen & seen
print(len(res))
result = sorted(res)
for i in result:
    print(i) 