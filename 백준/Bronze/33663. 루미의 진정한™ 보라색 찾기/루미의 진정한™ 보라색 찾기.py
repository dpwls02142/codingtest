import sys
sh, eh = map(int, sys.stdin.readline().rstrip().split())
ss, es = map(int, sys.stdin.readline().rstrip().split())
sv, ev = map(int, sys.stdin.readline().rstrip().split())
r, g, b = map(int, sys.stdin.readline().rstrip().split())
v = max(r, g, b)
s = 255 * ((v - min(r, g, b)) / v)
if v == r:
    h = ((60 * (g - b)) / (r - min(r, g, b)))
elif v == g:
    h = 120 + ((60 * (b - r)) / (g - min(r, g, b)))
elif v == b:
    h = 240 + ((60 * (r - g)) / (b - min(r, g, b)))
if h < 0:
    h += 360
# print(h, s, v)
if (sh <= h <= eh) and (ss <= s <= es) and (sv <= v <= ev):
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")