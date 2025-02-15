def solution(sides):
    max_line = max(sides)
    other = sum(sides) - max_line
    cnt = 0
    
    for i in range(max_line - other + 1, max_line + 1):
        cnt += 1
    for i in range(max_line + 1, sum(sides)):
        cnt += 1

    return cnt