import sys
from collections import deque
stack = deque()
t = int(sys.stdin.readline().rstrip())
for _ in range (t):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if len(command) > 1:
        c, n = command[0], int(command[1])
        if c == "push":
            stack.appendleft(n)
    else:
        c = command[0]
        if c == "pop":
            if len(stack) > 0:
                print(stack.popleft())
            else:
                print(-1)
        elif c == "size":
            print(len(stack))
        elif c == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif c == "top":
            if len(stack) > 0:
                print(stack[0])
            else:
                print(-1)