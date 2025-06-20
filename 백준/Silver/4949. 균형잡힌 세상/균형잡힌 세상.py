import sys
input = sys.stdin.readline
while True:
    lst = list(input().rstrip())
    if lst[0] == ".":
        break
    stack = []
    temp = True
    for i in lst:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                temp = False
                break
            stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                temp = False
                break
            stack.pop()
    if stack:
        temp = False
    if temp:
        print("yes")
    else:
        print("no")
