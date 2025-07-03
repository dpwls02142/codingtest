import sys
input = sys.stdin.readline
n = int(input().rstrip())
count = 0
num = 1
while True:
    if '666' in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1