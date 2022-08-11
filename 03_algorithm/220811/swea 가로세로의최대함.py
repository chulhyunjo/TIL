for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0
    for i in range(n):
        for j in range(n):
            sum1 = arr[i][j]
            for m in range(4):
                cnt = 1
                while True:
                    nx = i + dx[m] * cnt
                    ny = j + dy[m] * cnt

                    if 0 <= nx < n and 0 <= ny < n:
                        sum1 += arr[nx][ny]
                        cnt += 1
                    else:
                        break
            result = sum1 if result < sum1 else result

    print(f'#{tc} {result}')