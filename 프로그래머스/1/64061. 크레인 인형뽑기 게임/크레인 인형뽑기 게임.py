def solution(board, moves):
    ans = []
    removed = 0
    for a in moves:
        col = a - 1 
        for row in range(len(board)):
            if board[row][col] != 0:
                if ans and ans[-1] == board[row][col]:
                    ans.pop()
                    removed += 2 
                else:
                    ans.append(board[row][col])
                board[row][col] = 0
                break
         
    return removed