for tc in range(1, int(input())+1):
    day = list(range(7,0,-1))
    today = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    n = input()
    result = day[today.index(n)]
    print(f'#{tc} {result}')