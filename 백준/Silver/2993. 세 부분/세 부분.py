import sys
input = sys.stdin.readline
s = input().rstrip()
res = None
for i in range (1, len(s)-1):
    for j in range (i+1, len(s)):
        temp = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if res is None or temp < res:
            res = temp
print(res)