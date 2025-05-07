import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
j = int(input().rstrip())
fall = []
for _ in range (j):
    fall.append(int(input().rstrip()))
left = 1
right = m
res = 0
for i in fall:
    if left <= i <= right:
        continue
    elif i < left:
        move = left - i
        res += move
        left -= move
        right -= move
    elif i > right:
        move = i - right
        res += move
        left += move
        right += move
print(res)