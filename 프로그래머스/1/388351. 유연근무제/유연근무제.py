def solution(schedules, timelogs, startday):
    cnt = 0
    
    days = [(startday + i - 1) % 7 + 1 for i in range(7)]

    for schedule, logs in zip(schedules, timelogs):
        hour = schedule // 100
        minute = schedule % 100
        minute += 10
        if minute >= 60:
            minute -= 60
            hour += 1
        max_time = hour * 100 + minute
        
        valid = True
        
        for day, log in zip(days, logs):
            if day in [6, 7]:  # 주말은 평가에서 제외
                continue
            if log > max_time:  # 평일에 설정 시각 + 10분을 넘기면 불합격
                valid = False
                break
        
        if valid:
            cnt += 1

    return cnt