import sys
s = sys.stdin.readline().rstrip()
cnt_0 = 0
cnt_1 = 1
for i in s:
    if i == "0":
        cnt_0 += 1
    else:
        cnt_1 += 1

new_0 = (cnt_0 // 2) * "0"
new_1 = (cnt_1 // 2) * "1"
res = ''.join(map(str,(new_0, new_1)))
print(res)