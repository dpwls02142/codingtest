def solution(n, tops):

    MOD = 10007
    dp_s = [0] * n
    dp_o = [0] * n

    if tops[0] == 1:
        dp_s[0] = 4
        dp_o[0] = 3
    else:
        dp_s[0] = 3
        dp_o[0] = 2

    for i in range(1, n):
        if tops[i] == 1:
            dp_s[i] = ((dp_s[i-1] * 3) + dp_o[i-1]) % MOD
            dp_o[i] = ((dp_s[i-1] * 2) + dp_o[i-1]) % MOD
        else:
            dp_s[i] = (dp_s[i-1] * 2 + dp_o[i-1]) % MOD
            dp_o[i] = (dp_s[i-1] + dp_o[i-1]) % MOD

    return dp_s[-1]