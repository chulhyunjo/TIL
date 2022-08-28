for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    move = 0
    cnt = 1
    i = j = 0
    while cnt <= n * n:
        if arr[i][j] == 0:
            arr[i][j] = cnt
            cnt += 1

        nx = i + dx[move]
        ny = j + dy[move]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            i, j = nx, ny
        else:
            move = (move + 1) % 4
            i, j = i + dx[move], j + dy[move]

    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()