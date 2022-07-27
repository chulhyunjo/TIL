for tc in range(1, int(input())+1):
    n = int(input())
    array = [list(input()) for _ in range(n)]
    result = 'NO'
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for x in range(n):
        for y in range(n):
            if array[x][y] == 'o':
                for move in range(8):
                    cnt = 1
                    nx = x + dx[move]
                    ny = y + dy[move]
                    while 0<=nx<n and 0<=ny<n:
                        if array[nx][ny] != 'o':
                            break
                        cnt += 1
                        nx += dx[move]
                        ny += dy[move]
                        if cnt == 5:
                            result = 'YES'
    print(f'#{tc} {result}')