import sys
n = int(sys.stdin.readline().rstrip())
room = []
for _ in range (n):
    room.append(list(sys.stdin.readline().rstrip()))
row_res, col_res = 0, 0
for i in range (n):
    row_cnt = 0
    for j in range (n):
        if room[i][j] == ".":
            row_cnt += 1
        else:
            if row_cnt >= 2:
                row_res += 1
            row_cnt = 0
    if row_cnt >= 2:
        row_res += 1
for i in range (n):
    col_cnt = 0
    for j in range (n):
        if room[j][i] == ".":
            col_cnt += 1
        else:
            if col_cnt >= 2:
                col_res += 1
            col_cnt = 0
    if col_cnt >= 2:
        col_res += 1
print(row_res, col_res)