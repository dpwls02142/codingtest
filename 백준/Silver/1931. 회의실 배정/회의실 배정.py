n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append([start, end])

meetings.sort(key=lambda x: (x[1], x[0]))

max_meetings = 0
end_time = 0

for meeting in meetings:
    if meeting[0] >= end_time:
        end_time = meeting[1]
        max_meetings += 1

print(max_meetings)