import sys
input = sys.stdin.readline
n = int(input().rstrip())
stack = []
res = 0
for _ in range (n):
    a = list(map(int, input().rstrip().split()))
    if a[0] == 1:
        score, time = a[1], a[2]
        stack.append([score, time])
    if stack:
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            res += stack[-1][0]
            stack.pop()
            
print(res)