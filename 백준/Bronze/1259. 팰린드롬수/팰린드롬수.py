import sys

while True:
    a = sys.stdin.readline().rstrip()
    if a == '0':
        break
    else:
        b = a[::-1]
        if a != b:
            print('no')
        else:
            print('yes')