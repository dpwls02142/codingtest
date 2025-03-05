import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))

res = [-1] * n
stack = []

for i in range(n):  
    while stack and a[stack[-1]] < a[i]:
        res[stack.pop()] = a[i]
    stack.append(i)  # 현재 "인덱스"를 스택에 저장

print(*res)