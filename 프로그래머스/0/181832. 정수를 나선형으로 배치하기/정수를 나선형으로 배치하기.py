def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1
    num = 1
    
    for _ in range(n * n):
        answer[x][y] = num
        num += 1
        
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            dx, dy = dy, -dx
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny
    
    return answer