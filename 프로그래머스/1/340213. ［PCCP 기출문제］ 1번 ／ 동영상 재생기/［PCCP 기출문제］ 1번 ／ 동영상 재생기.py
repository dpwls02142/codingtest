def solution(video_len, pos, op_start, op_end, commands):
    def to_sec(time_str):
        m, s = map(int, time_str.split(":"))
        return m * 60 + s

    video_sec = to_sec(video_len)
    pos_sec = to_sec(pos)
    op_start_sec = to_sec(op_start)
    op_end_sec = to_sec(op_end)

    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for cmd in commands:
        if cmd == "next":
            if video_sec - pos_sec < 10:
                pos_sec = video_sec
            else:
                pos_sec += 10
        else:
            pos_sec = max(0, pos_sec - 10)

        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return f"{pos_sec // 60:02}:{pos_sec % 60:02}"