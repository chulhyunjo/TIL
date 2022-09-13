for tc in range(1, int(input()) + 1):
    results = input()
    cnt = 0
    for result in results:
        if result == 'x':
            cnt += 1
    print(f'#{tc}', end = ' ')
    if cnt >= 8:
        print('NO')
    else:
        print('YES')