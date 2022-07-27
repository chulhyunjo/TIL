for tc in range(1, int(input()) + 1):
    n = int(input())
    array = [list(input()) for _ in range(n)]
    x = y = x2 = y2 = 0
    result = ''
    for i in range(n):
        for j in range(n):
            if array[i][j] == '#':
                x, y = i, j
                break
        if (x,y) == (i,j):
            break

    for a in range(n-1, -1 , -1):
        for b in range(n-1, -1, -1):
            if array[a][b] == '#':
                x2, y2 = a, b
                break
        if (x2, y2) == (a, b):
            break

    print(f'#{tc}', end = ' ')
    if x2 - x != y2 - y:
        result = 'no'

    else:
        for i in range(x2 - x + 1):
            for j in range(y2 - y + 1):
                if array[x + i][y + j] != '#':
                    result = 'no'
                    break
            if result == 'no':
                break
        else:
            result = 'yes'
    print(result)`