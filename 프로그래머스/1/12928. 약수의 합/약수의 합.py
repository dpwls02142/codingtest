def solution(n):
    ans = 0
    for i in range (1, n+1):
        for j in range (1, n+1):
            if i * j == n:
                ans += i
    return ans