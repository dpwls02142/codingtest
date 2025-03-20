def solution(n, lost, reserve):
    ans = [1] * n  
    answer = 0
    for l in lost:
        ans[l - 1] -= 1

    for r in reserve:
        ans[r - 1] += 1

    for i in range(n):
        if ans[i] == 0:
            if i > 0 and ans[i - 1] == 2:
                ans[i - 1] -= 1
                ans[i] += 1
            elif i < n - 1 and ans[i + 1] == 2:
                ans[i + 1] -= 1
                ans[i] += 1

    for i in range (len(ans)):
        if ans[i] >= 1:
            answer += 1
    return answer
