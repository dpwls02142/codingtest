def solution(N, number):
    dp = [set() for _ in range(9)]

    # i개의 N으로 만들 수 있는 초기값
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    # 1부터 8까지의 사용 횟수에 대해 탐색
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        
        if number in dp[i]:
            return i
    
    return -1