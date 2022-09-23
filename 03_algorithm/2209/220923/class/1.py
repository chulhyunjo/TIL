T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    cell = [['/'] * N] + [['/'] + ['0'] * (N - 2) + ['/'] for _ in range(N - 2)] + [['/'] * N]
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    for _ in range(K):
        x, y, bug_num, direction = map(int, input().split())
        cell[x][y] = [bug_num, direction]

    for m in range(M):
        after_cell = [['/'] * N] + [['/'] + ['0'] * (N - 2) + ['/'] for _ in range(N - 2)] + [['/'] * N]
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                visited[i][j] = [(0, 0)]

        for x in range(N):
            for y in range(N):
                if len(cell[x][y]) == 3:
                    nx = x + dx[cell[x][y][1]]
                    ny = y + dy[cell[x][y][1]]
                    if len(after_cell[nx][ny]) == 2:
                        cell[x][y].pop()
                        visited[nx][ny].append(tuple(cell[x][y]))
                        visited[nx][ny].sort()
                        after_cell[nx][ny][1] = visited[nx][ny][-1][-1]
                        after_cell[nx][ny][0] = cell[x][y][0] + after_cell[nx][ny][0]
                    else:
                        cell[x][y].pop()
                        after_cell[nx][ny] = cell[x][y]
                        visited[nx][ny].append(tuple(cell[x][y]))
                elif len(cell[x][y]) == 2:
                    nx = x + dx[cell[x][y][1]]
                    ny = y + dy[cell[x][y][1]]
                    if len(after_cell[nx][ny]) == 2:
                        visited[nx][ny].append(tuple(cell[x][y]))
                        visited[nx][ny].sort()
                        after_cell[nx][ny][1] = visited[nx][ny][-1][-1]
                        after_cell[nx][ny][0] = cell[x][y][0] + after_cell[nx][ny][0]
                    elif after_cell[nx][ny] == '/':
                        cell[x][y].append('/')
                        after_cell[nx][ny] = cell[x][y]
                        after_cell[nx][ny][0] = cell[x][y][0] // 2
                        if cell[x][y][1] == 1:
                            t = 2
                        elif cell[x][y][1] == 2:
                            t = 1
                        elif cell[x][y][1] == 3:
                            t = 4
                        elif cell[x][y][1] == 4:
                            t = 3
                        after_cell[nx][ny][1] = t
                        if cell[x][y][0] // 2 == 0:
                            after_cell[nx][ny] = '/'
                    else:
                        after_cell[nx][ny] = cell[x][y]
                        visited[nx][ny].append(tuple(cell[x][y]))

        cell = after_cell

    sum1 = 0
    for i in range(N):
        for j in range(N):
            if len(cell[i][j]) >= 2:
                sum1 += cell[i][j][0]

    print(f'#{tc} {sum1}')