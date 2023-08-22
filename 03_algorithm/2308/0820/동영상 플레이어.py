def solution(video_len, pos, op_start, op_end, commands):
    video_len = video_len.split(':')
    length = int(video_len[0]) * 60 + int(video_len[1])

    pos = pos.split(':')
    now = int(pos[0]) * 60 + int(pos[1])

    op_start = op_start.split(':')
    start = int(op_start[0]) * 60 + int(op_start[1])

    op_end = op_end.split(':')
    end = int(op_end[0]) * 60 + int(op_end[1])

    if start <= now < end:
        now = end

    for command in commands:
        if command == 'prev':
            now = now - 10 if now >= 10 else 0

        elif command == 'next':
            now = now + 10 if now + 10 < length else length

        if start <= now < end:
            now = end

    minute = str(now // 60)
    second = str(now % 60)

    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second

    return f'{minute}:{second}'