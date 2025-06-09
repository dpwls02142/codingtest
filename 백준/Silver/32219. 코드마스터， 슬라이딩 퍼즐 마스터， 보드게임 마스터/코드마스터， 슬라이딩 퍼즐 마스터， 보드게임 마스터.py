import sys
input = sys.stdin.readline
# 이동 가능 범위: lst[r-n][c] or lst[r][c-n]  n: 1 <= n
t = int(input().rstrip())
for _ in range (t):
    r, c = map(int, input().rstrip().split())
    if r ^ c == 0:
        print("dohoon")
    else:
        print("jinseo")
        target_r = r ^ (r ^ c)
        if 1 <= target_r < r:
            print(target_r, c)
        else:
            print(r, (c ^ (r ^ c)))