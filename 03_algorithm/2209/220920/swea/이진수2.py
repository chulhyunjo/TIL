for tc in range(1, int(input())+1):
    n = float(input())
    result = ''
    i = 1
    while n:
        if i > 12:
            result = 'overflow'
            break
        if n >= 2**(-i):
            n -= 2**(-i)
            result += '1'
        else:
            result += '0'
        i += 1
    print(f'#{tc} {result}')
