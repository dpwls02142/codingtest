# seq 안에 있는 i의 요소가 stack 연산만으로 나올 수 있는지 없는지 판단
# i가 이미 stack안에 포함되어있는데 top에 위치해있지 않다면 false
# => 1부터 n까지의 수를 스택에 넣었다가 "뽑아" 늘어놓는다고 했으니까
import sys
n = int(sys.stdin.readline().rstrip())
seq = [int(sys.stdin.readline().rstrip()) for _ in range (n)]

stack, res = [], []
current = 1
valid = False

for i in seq:
    while current <= i:
        stack.append(current)
        res.append("+")
        current += 1
    if stack[-1] == i:
        stack.pop()
        res.append("-")
    else:
        valid = True
        break
    
if valid:
    print("NO")
else:
    for i in res:
        print(i)