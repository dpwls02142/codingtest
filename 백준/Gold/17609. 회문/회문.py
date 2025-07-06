import sys
input = sys.stdin.readline
def palin(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
t = int(input().rstrip())
for _ in range (t):
    s = input().rstrip()
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            if palin(s, l + 1, r) or palin(s, l, r - 1):
                print(1)
            else:
                print(2)
            break
        l += 1
        r -= 1
    else:
        print(0)