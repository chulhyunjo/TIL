for tc in range(1, int(input())+1):
    n = int(input())

    arr = [list(input()) for _ in range(n)]
    dx = [1,0,1,1]
    dy = [0,1,1,-1]
    result = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                x, y = i, j
                for q in range(4):
                    cnt = 1
                    for w in range(1,5):
                        nx = x + dx[q] * w
                        ny = y + dy[q] * w
                        if 0 > nx or nx >= n or ny < 0 or ny >= n:
                            break
                        if arr[nx][ny] != 'o':
                            break
                        cnt += 1
                    if cnt == 5:
                        result = 1
                        break
            if result: break
        if result: break

    if result:
        print(f"#{tc} YES")
    else:
        print(f'#{tc} NO')