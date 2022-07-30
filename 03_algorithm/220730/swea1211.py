dx = [0, 0, -1]
dy = [-1, 1, 0]

for t in range(10):
    tc = int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]
    min_move = 999999
    cnt = 99999
    x = y = 0
    result = 0

    for i in range(100):
        if ladder[99][i] == 1:
            x, y = 99, i
            visited = {(x, y)}
            cnt = 1
            while x>0:
                for move in range(3):
                    nx = x + dx[move]
                    ny = y + dy[move]

                    if (nx,ny) in visited:
                        continue

                    if nx == -1 or ny == 100 or ny == -1:
                        continue

                    if ladder[nx][ny] == 1:
                        cnt += 1
                        visited.add((nx, ny))
                        x, y = nx, ny
                        break

        min_move = min(min_move, cnt)
        if min_move == cnt:
            result = y
    print(f'#{tc} {result}')