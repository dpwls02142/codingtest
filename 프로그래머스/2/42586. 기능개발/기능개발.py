# 14:15
from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    d = deque(progresses)
    s = deque(speeds)
    while d:
        cnt = 0
        a = d.popleft()
        b = s.popleft()
        while a < 100:
            a += b
            cnt += 1
        days.append(cnt)
    while days:
        base_day = days.popleft()
        count = 1
        while days and days[0] <= base_day:
            days.popleft()
            count += 1
        answer.append(count)
    return answer