def solution(p, n):
    # 시간 포멧
    def formatTime(time):
        if time < 10:
            return '0' + str(time)
        else:
            return str(time)

    # p[0] = 'AM','PM', p[1] = 시간
    p = p.split()
    time = list(map(int, p[1].split(":")))

    # 현재 시간을 초로 바꾸기
    second = time[0] * 3600 + time[1] * 60 + time[2]

    # 24시간 형식으로 변경
    if time[0] == 12:
        if p[0] == 'AM':
            second -= 3600 * 12
    elif p[0] == 'PM':
        second += 3600 * 12

    # N초 더하고 시간 변경
    second += n
    hour = (second // 3600) % 24
    second %= 3600
    minute = second // 60
    second %= 60

    # 출력 형식으로 변경
    hour = formatTime(hour)
    minute = formatTime(minute)
    second = formatTime(second)

    return f'{hour}:{minute}:{second}'
