def solution(triangle):

    dp = [row[:] for row in triangle]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])): # 0 1 2
            if j > 0: # 0
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j])
            if j < i: # 2
                dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
    
    return max(dp[-1])