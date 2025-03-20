import sys
s = sys.stdin.readline().rstrip()
# 1이 연속해서 나온 횟수 vs 0이 연속해서 나온 횟수 
# 더 작은거를 반환하면 됨
one_cnt = 0
zero_cnt = 0
if s[0] == "0":
    zero_cnt += 1
else:
    one_cnt += 1
for i in range (1, len(s)):
    if s[i] != s[i - 1]:
        if s[i] == "0":
            zero_cnt += 1
        else:
            one_cnt += 1
# print(one_cnt, zero_cnt)
if zero_cnt > one_cnt:
    print(one_cnt)
elif zero_cnt < one_cnt:
    print(zero_cnt)
elif zero_cnt == one_cnt:
    print(one_cnt)