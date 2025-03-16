import sys
round = int(sys.stdin.readline().rstrip())
c_score, s_score = 100, 100
for i in range (round):
    c_dice, s_dice = map(int, sys.stdin.readline().rstrip().split())
    if c_dice > s_dice:
        s_score -= c_dice
    elif s_dice > c_dice:
        c_score -= s_dice
    elif c_dice == s_dice:
        continue
print(c_score)
print(s_score)