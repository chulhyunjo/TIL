for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())                            # 배열크기, 파리채크기 입력
    arr = [list(map(int, input().split())) for _ in range(n)]   # 영역 입력
    result = 0
    for i in range(n - m + 1):                                  # 영역 탐색
        for j in range(n - m + 1):
            sum1 = 0                                            # 현재 범위의 파리 개수
            for k in range(m):                                  # mxm 파리채 범위 탐색
                for l in range(m):
                    sum1 += arr[i + k][j + l]                   # 파리 개수 더하기
            result = sum1 if result < sum1 else result          # 파리개수가 더 많으면 result 담기

    print(f'#{tc} {result}')
