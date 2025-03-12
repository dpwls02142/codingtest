import sys
n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
ps = ["PS4", "PS5"]
while True:
    if ps[0] in s:
        s = s.replace(ps[0], "PS")
    elif ps[1] in s:
        s = s.replace(ps[1], "PS")
    else:
        break
print(s)