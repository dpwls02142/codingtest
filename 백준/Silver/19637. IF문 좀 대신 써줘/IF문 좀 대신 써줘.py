import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
skills = []
res = []
for _ in range (n):
    skill_name, skill_maximum = map(str, sys.stdin.readline().rstrip().split())
    skills.append((skill_name, int(skill_maximum)))
# 점수를 기준으로 sort
skills.sort(key=lambda x: x[1])
for _ in range (m):
    power = int(sys.stdin.readline().rstrip())
    left, right = 0, n-1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if skills[mid][1] >= power:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    if answer != -1:
        res.append(skills[answer][0])
for i in res:
    print(i)