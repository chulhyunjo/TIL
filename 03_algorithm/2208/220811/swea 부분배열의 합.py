for tc in range(1,int(input())+1):
    N, n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N-n+1):
        for j in range(N-m+1):
            sum1 = 0
            for k in range(n):
                for l in range(m):
                    sum1 += arr[i+k][j+l]

            result = sum1 if result < sum1 else result

    print(f'#{tc} {result}')