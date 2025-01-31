import sys

# 종말의 수란 6이 3개 이상 연속으로 들어가는 수
a = int(sys.stdin.readline().rstrip())
cnt = 0
num = 666

while True:
    if '666' in str(num):
        cnt += 1
        if cnt == a:
            print(num)
            break
    num += 1