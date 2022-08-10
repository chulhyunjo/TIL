for tc in range(1,int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    for i in range(n):
        for j in range(m):
            sum1 = arr[i][j]
            for k in range(4):
                for x in range(1, arr[i][j]+1):
                    nx = i + dx[k] * x
                    ny = j + dy[k] * x

                    if 0 <= nx < n and 0 <= ny < m:
                        sum1 += arr[nx][ny]
            if result < sum1:
                result = sum1
    print(f'#{tc} {result}')