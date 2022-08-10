for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    result = 0
    sum_dia1 = 0
    sum_dia2 = 0
    for i in range(100):
        sum_col = 0
        sum_row = 0
        for j in range(100):
            sum_col += arr[i][j]
            sum_row += arr[j][i]
        sum_dia1 += arr[i][i]
        sum_dia2 += arr[i][100-i-1]
        if result < sum_col:
            result = sum_col
        if result < sum_row:
            result = sum_row

    if result < sum_dia1:
        result = sum_dia1
    if result < sum_dia2:
        result = sum_dia2

    print(f'#{tc} {result}')