dx = [1, 0]
dy = [0, 1]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            col = row = 1
            if arr[i][j] == 1:
                now_i, now_j = i, j
                while True:
                    nx = now_i + dx[0]
                    ny = now_j + dy[0]
                    if arr[nx][ny] == 0:
                        break
                    col += 1
                    now_i, now_j = nx, ny
                now_i, now_j = i, j
                while True:
                    nx = now_i + dx[1]
                    ny = now_j + dy[1]
                    if arr[nx][ny] == 0:
                        break
                    row += 1
                    now_i, now_j = nx, ny
            area = col * row
            result = area if result < area else result
    print(f'#{tc} {result}')