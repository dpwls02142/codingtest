import sys
input = sys.stdin.readline
t = int(input())
for _ in range (t):
    n = int(input())
    s = input().rstrip()
    minus_pos = s.find('-')
    if minus_pos == -1:
        print("YES")
        continue
    
    minus_pos += 1
    while minus_pos < len(s) and s[minus_pos].isdigit():
        minus_pos += 1
    ok = True
    for i in range(minus_pos, len(s)):
        if '1' <= s[i] <= '9':
            ok = False
            break
    print("YES" if ok else "NO")