from collections import defaultdict
import sys
input = sys.stdin.readline
a = int(input().rstrip())
students = []
for _ in range (a):
    team, num, score = map(int, input().rstrip().split())
    students.append((team, num, score))
students.sort(key=lambda x: -x[2])
team_count = defaultdict(int)
cnt = 0
for team, num, score in students:
    if team_count[team] < 2:
        print(team, num)
        team_count[team] += 1
        cnt += 1
    if cnt == 3:
        break