import sys
input = sys.stdin.readline
lst = list(input().rstrip())
res = 0
t = 0
for i in range (12):
    if lst[i] == "*":
        t = i + 1
    elif ((i + 1) % 2) == 0:
        res += int(lst[i]) * 3
    elif ((i + 1) % 2) != 0:
        res += (int(lst[i]))
cnt = 0
while True:
    if t % 2 == 0:
        test_res = res + (cnt * 3)
    else:
        test_res = res + cnt
    temp = 10 - test_res % 10
    if temp == 10:
        temp = 0
    if int(lst[-1]) == temp:
        print(cnt)
        break
    else:
        cnt += 1