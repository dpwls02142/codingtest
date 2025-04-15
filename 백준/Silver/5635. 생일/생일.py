import sys
t = int(sys.stdin.readline().rstrip())
student = []
for _ in range (t):
    name, day, month, year = map(str, sys.stdin.readline().rstrip().split())
    day, month, year = int(day), int(month), int(year)
    student.append([name, day, month, year])
student.sort(key=lambda x : (x[3], x[2], x[1]))
print(student[-1][0])
print(student[0][0])