for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dz1 = [1,1,-1,-1]
    dz2 = [-1,1,1,-1]

    result = 0
    for i in range(n):
        for j in range(n):
            sum1 = arr[i][j]
            sum2 = arr[i][j]
            for q in range(4):
                for w in range(1,m):
                    nx = i + dx[q] * w
                    ny = j + dy[q] * w
                    nz1 = i + dz1[q] * w
                    nz2 = j + dz2[q] * w
                    if 0 <= nx < n and 0 <= ny < n:
                        sum1 += arr[nx][ny]

                    if 0 <= nz1 < n and 0 <= nz2 < n:
                        sum2 += arr[nz1][nz2]
            if result < sum1:
                result = sum1
            if result < sum2:
                result = sum2
    print(f'#{tc} {result}')