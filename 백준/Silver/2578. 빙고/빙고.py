import sys
player = []
for _ in range (5):
    player.append(list(map(int, sys.stdin.readline().rstrip().split())))
calls = []
for _ in range (5):
    calls.append(list(map(int, sys.stdin.readline().rstrip().split())))
cnt = 0
for i in range(5):
    for j in range(5):
        num = calls[i][j]
        cnt += 1
        for x in range(5):
            for y in range(5):
                if player[x][y] == num:
                    player[x][y] = 0
        res = 0
        for x in range (5):
            if player[x] == [0, 0, 0, 0, 0]:
                res += 1
        for x in range (5):
            valid = True
            for y in range (5):
                if player[y][x] != 0:
                    valid = False
                    break
            if valid:
                res += 1
        valid = True
        for d in range (5):
            if player[d][d] != 0:
                valid = False
                break
        if valid:
            res += 1
        valid = True
        for d in range (5):
            if player[d][4-d] != 0:
                valid = False
                break
        if valid:
            res += 1
        if res >= 3:
            print(cnt)
            sys.exit()