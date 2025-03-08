import sys

n = int(sys.stdin.readline().rstrip())
cookie = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

head_x, head_y = 0, 0
flag = False
for i in range(n):
    for j in range(len(cookie[i])):
        if cookie[i][j] == "*":
            head_x, head_y = i, j
            flag = True
            break
    if flag:
        break

heart_x, heart_y = head_x + 1, head_y

left_arm = 0
for j in range(heart_y - 1, -1, -1):
    if cookie[heart_x][j] == "*":
        left_arm += 1
    else:
        break

right_arm = 0
for j in range(heart_y + 1, n):
    if cookie[heart_x][j] == "*":
        right_arm += 1
    else:
        break

waist = 0
waist_end_x = 0 
for i in range(heart_x + 1, n):
    if cookie[i][heart_y] == "*":
        waist += 1
        waist_end_x = i
    else:
        break

left_leg = 0
for i in range(waist_end_x + 1, n):
    if cookie[i][heart_y - 1] == "*":
        left_leg += 1
    else:
        break

right_leg = 0
for i in range(waist_end_x + 1, n):
    if cookie[i][heart_y + 1] == "*":
        right_leg += 1
    else:
        break

print(heart_x + 1, heart_y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)