import sys
# 최대값을 구하는거니까 무조건 앞에서부터 시작해야됨.
# 메모리 사용량: 제너레이터 < 리스트 컴프리헨션
s = int(sys.stdin.readline().rstrip())
a = (_ for _ in range(1, (s + 1)))
res = 0
cnt = 0
for i in a:
    res += i
    if res == s:
        cnt += 1
        break
    elif res >= s:
        break
    else:
        cnt += 1
print(cnt)