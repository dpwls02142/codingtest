import sys
input = sys.stdin.readline
n = int(input().rstrip())
roll = {}
for _ in range (n):
    name, score, risk, cost = map(str, input().rstrip().split())
    score, risk, cost = int(score), int(risk), int(cost)
    scholarshipScore =  ((score**3) // (cost * (risk + 1)))
    roll[name] = (scholarshipScore, cost)
roll = sorted(roll.items(), key=lambda item: (-item[1][0], item[1][1], item[0], len(item[0])))
print(roll[1][0])