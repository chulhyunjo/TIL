for tc in range(int(input())):
    n, m = map(int, input().split())
    array = [list(input()) for _ in range(n)]
    black = [] # '#' 리스트
    white = [] # '.' 리스트

    for i in range(n):
        for j in range(m):
            if array[i][j] == '#':
                black.append((i + j) % 2)
            if array[i][j] == '.':
                white.append((i + j) % 2)

    b, w = len(set(black)), len(set(white))
    print(f'#{tc+1}', end = ' ')
    if b > 1 or w > 1:
        print('impossible')
    elif b == 1 and w == 1:
        if set(black) == set(white):
            print('impossible')
        else:
            print('possible')
    else:
        print('possible')