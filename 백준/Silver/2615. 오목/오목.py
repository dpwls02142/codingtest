import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def is_valid(x, y):
    return 0 <= x < 19 and 0 <= y < 19

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            color = board[x][y]
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                cnt = 1

                while is_valid(nx, ny) and board[nx][ny] == color:
                    cnt += 1
                    if cnt > 5:
                        break
                    nx += dx[d]
                    ny += dy[d]

                if cnt == 5:
                    px = x - dx[d]
                    py = y - dy[d]
                    if is_valid(px, py) and board[px][py] == color:
                        continue 
                    
                    print(color)
                    print(x + 1, y + 1)
                    sys.exit()

print(0)
