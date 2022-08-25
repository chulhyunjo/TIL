for _ in range(10):
    tc = int(input())
    maz = [list(map(int,input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maz[i][j] == 2:
                x, y = i, j

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = []
    queue.append((x,y))
    result = 0
    while queue:
        x, y = queue.pop(0)

        for q in range(4):
            nx = x + dx[q]
            ny = y + dy[q]

            if 0 > nx or 16 <= nx or 0 > ny or 16 <= ny or maz[nx][ny] == 1:
                continue
            if maz[nx][ny]== 3:
                result = 1
                break
            queue.append((nx,ny))
            maz[nx][ny] = 1

        if result:
            break
    print(f'#{tc} {result}')