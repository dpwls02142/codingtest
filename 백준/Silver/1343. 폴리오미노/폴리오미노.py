import sys
board = list(sys.stdin.readline().rstrip())
i = 0
n = len(board)
res = []
while i < n:
    if board[i] == 'X':
        cnt = 0
        while i < n and board[i] == 'X':
            cnt += 1
            i += 1   
        if cnt % 2 != 0:
            print(-1)
            exit()
        res.append("AAAA" * (cnt // 4) + "BB" * ((cnt % 4) // 2))
    else:
        res.append('.')
        i += 1
print("".join(res))