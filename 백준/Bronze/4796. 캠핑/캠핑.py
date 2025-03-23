import sys
# 20일짜리 휴가 시작.
# 8일 중에 5일만 사용 가능.
# 8 + 8 + 4 = 5 + 5 + 4 = 14
c = 1
while True:
    l, p, v = map(int, sys.stdin.readline().rstrip().split())
    if l == 0 and p == 0 and v == 0:
        break
    period = v // p # 2
    a = min((v % p), l) # 4, 5
    res = (period * l) + a # 5 * 2 + a
    print(f'Case {c}: {res}')
    c += 1