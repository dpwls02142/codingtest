import sys

a = sys.stdin.readline().rstrip()
a = a.upper()

cnt = {}
res = ""

for i in a:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1

max_cnt = max(cnt.values())

count_max = 0
most_common_char = ""

for key, value in cnt.items():
    if value == max_cnt:
        count_max += 1
        most_common_char = key

if count_max > 1:
    res = "?"
else:
    res = most_common_char

print(res)