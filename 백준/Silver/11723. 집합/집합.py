import sys

n = int(sys.stdin.readline().rstrip())
com = ['add', 'remove', 'check', 'toggle', 'all', 'empty']
s = set()

for i in range (n):
    line = sys.stdin.readline().rstrip().split()

    if line[0] in com[:4]:  # 'add', 'remove', 'check', 'toggle' 명령은 b 값이 필요
        a, b = line
        b = int(b)
    else:  # 'all'과 'empty' 명령은 b 값을 받지 않음
        a = line[0]

    if a == com[0]:
        s.add(b)
    elif a == com[1]:
        s.discard(b) # discard는 안에 값이 없을 때 지운다고해도 오류 발생 X
    elif a == com[2]:
        if b in s:
            print(1)
        else:
            print(0)
    elif a == com[3]:
        if b in s:
            s.remove(b)
        else:
            s.add(b)
    elif a == com[4]:
        s = set(range(1,21))
    else:
        s = set()
