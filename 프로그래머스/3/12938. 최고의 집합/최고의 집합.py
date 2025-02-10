def solution(n, s):
    if s < n:
        return [-1]
    
    a = s // n
    b = s % n
    
    res = [a] * n
    
    for i in range (b):
        res[-(i+1)] += 1
    
    return res