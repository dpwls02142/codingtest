def solution(n):
    ans = 0
    a = [x for x in range (4, n+1)]
    for i in a:
        cnt = 0
        for j in range (1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >= 3:
            ans += 1

    return ans