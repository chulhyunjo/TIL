for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            sum1 = 0
            for k in range(m):
                for l in range(m):
                    sum1 += arr[i + k][j + l]
            result = sum1 if result < sum1 else result

    print(f'#{tc} {result}')
