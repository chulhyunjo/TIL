for tc in range(1, int(input())+1):
    n, k = map(int,input().split())                             # n:배열크기 k:구간크기
    arr = [list(map(int,input().split())) for _ in range(n)]    # 2중 배열
    result = 0                                                  # 결과값

    for i in range(n):
        sum1 = 0
        for j in range(k):
            if i + j >= n:                                      # 인덱스 오류 방지
                continue
            sum1 += arr[i][i+j]

        result = sum1 if sum1 > result else result

    print(f'#{tc} {result}')