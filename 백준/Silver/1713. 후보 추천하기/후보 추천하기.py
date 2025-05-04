import sys
input = sys.stdin.readline
from collections import deque
n = int(input().rstrip())
thumbs = int(input().rstrip())
thumbs_list = deque(map(int, input().split()))

photo = {}
res = []

for student in thumbs_list:
    if student in photo:
        photo[student] += 1
    else:
        if len(res) < n:
            photo[student] = 1
            res.append(student)
        else:
            min_votes = min(photo[s] for s in res)
            for old in res:
                if photo[old] == min_votes:
                    res.remove(old)
                    del photo[old]
                    break
            photo[student] = 1
            res.append(student)

print(*sorted(res))