import sys
input = sys.stdin.readline
import math
a, b, c = map(int, input().rstrip().split())
s, v = map(int, input().rstrip().split())
l = int(input().rstrip())

target_exp = (250 - l) * 100
curr_exp = 0
res = 0

order = sorted([
    (a, float('inf')),
    (b, s * 30),
    (c, v * 30)
], reverse=True)

for exp_min, ava_min in order:
    if curr_exp >= target_exp:
        break
    use_min = min(ava_min, math.ceil((target_exp - curr_exp) / exp_min))
    curr_exp += use_min * exp_min
    res += use_min
print(res)