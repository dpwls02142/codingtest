import sys
n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range (n):
    stack = list(sys.stdin.readline().rstrip())
    temp = []
    while stack:
        temp.append(stack.pop())
        if len(temp) >= 2 and temp[-1] == "(" and temp[0] == ")":
            temp.pop()
            temp.pop(0)
        if len(temp) == 0:
            valid = True
        else:
            valid = False
    if valid:
        print("YES")
    else:
        print("NO")