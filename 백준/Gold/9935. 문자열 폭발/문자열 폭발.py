import sys
input = sys.stdin.readline

s = input().rstrip()
boom = input().rstrip()
stack = []

for i in s:
    stack.append(i)
    if ''.join(stack[-len(boom):]) == boom:
        for _ in range (len(boom)):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")